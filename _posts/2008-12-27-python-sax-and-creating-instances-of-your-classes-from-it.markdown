---
comments: true
date: 2008-12-27 20:00:00
layout: post
slug: python-sax-and-creating-instances-of-your-classes-from-it
title: Python, SAX and creating instances of your classes from it
wordpress_id: 242
---

So I made up a small XML-Snippet to send data of of probes around. Basically it's just the information



	
  * which host collected data of

	
  * which probe,

	
  * when it was and

	
  * what it's value is.


What we could end up with in the worst case is an XML document of quite a few megabytes. Now to efficiently parse that thing I wanted to use something that doesn't need to keep the whole document in memory.

What I found was [sax](http://en.wikipedia.org/wiki/Simple_API_for_XML) and [expat](http://en.wikipedia.org/wiki/Expat_%28XML%29), both of which are available in the [python standard library](http://docs.python.org/library/index.html).

I chose to use sax as I didn't want to jump into XML to deep, and a bit of googling around suggestedSo what's the simplest way of using this SAX thing with python?

First let's define some sample data

    
    <?xml version="1.0" encoding="UTF-8"?>
    <itemList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
         <item hostName="host1.example.com" itemName="boolean item">
                 <dateRecorded>1967-08-13</dateRecorded>
                 <boolValue>true</boolValue>
         </item>
         <item hostName="host1.example.com" itemName="float item">
                 <dateRecorded>1967-08-13</dateRecorded>
                 <floatValue>1.2</floatValue>
         </item>
         <item hostName="host1.example.com" itemName="int item without time">
                 <dateRecorded>1967-08-13</dateRecorded>
                 <intValue>12</intValue>
         </item>
         <item hostName="host1.example.com" itemName="string item without time">
                 <dateRecorded>1967-08-13</dateRecorded>
                 <stringValue>foo</stringValue>
         </item>
    </itemList>


Now our first draft of using the SAX module in python. What you do with SAX essentially is:



	
  * import the needed modules

	
  * make a subclass of sax.ContentHandler

	
  * Later we will implement the methods for:



	
  * what to do when the document starts

	
  * what to do when the document ends

	
  * what to do when an element starts

	
  * what to do when an element ends

	
  * what to do with content of elements



    
    #!/usr/bin/env python
    # vim: syn=python ts=4 sts=4 enc=utf-8 tw=78 bg=dark expandtab:
    
    import os
    import sys
    from xml import sax
    class ItemListParser(sax.ContentHandler):
       pass
    sax.parse(sys.argv[1], ItemListParser())


No that code doesn't really do much except that it doesn't generate errors. Let's enhance it so that we at least get some info on what's happening

    
    #!/usr/bin/env python
    # vim: syn=python ts=4 sts=4 enc=utf-8 tw=78 bg=dark expandtab:
    
    import os
    import sys
    from xml import sax
    
    def emit(message):
       print message.encode("UTF-8")
    
    class ItemListParser(sax.ContentHandler):
       def startDocument(self):
           emit(u"The document has started")
       def endDocument(self):
           emit(u"The document has ended")
       def startElement(self, name, attrs):
           emit(u"A new element started: %s" % (name, ))
       def endElement(self, name):
           emit(u"A element ended: %s" % (name, ))
       def characters(self, content):
           emit(u"Content found: %s" % (repr(content), ))
    
    sax.parse(sys.argv[1], ItemListParser())


If you run this code you should be able to see how SAX works, it's actually just executing the method defined for an event. Now the good news is you don't need to worry about memory (mostly, that is). The bad news is that you don't really have any object like access so you need some sort of state to know when to do what. Let's create a simple class that will hold the values of your items defined in the XML sample

    
    class Item(object):
       def __init__(self, host, name, date_time, value):
           self.host = host
           self.name = name
           self.time = date_time
           self.value = value
    
       def __str__(self):
           return u'' % (self.__class__,
               self.host,
               self.name,
               self.time,
               self.value)


A simple data structure like Item class. The _hard part_ with SAX now is that you don't have access to the necessary parameters without some work to create an instance of the Item class. Let's fix that by first doing a step backwards and writing some documentation for the _ItemListParser_ class so that we have a plan of what we want.

    
    class ItemListParser(sax.ContentHandler):
       def startDocument(self):
           """We don't need anything special when the document starts."""
       def endDocument(self):
           """We don't need anything special when the document ends."""
       def startElement(self, name, attrs):
           """Save the state depending on the element encountered."""
       def endElement(self, name):
           """Clear the state depending on the element encountered, possibly
    create an instance of the desired object."""
       def characters(self, content):
           """Save the characters encountered to a helper variable depending on
    the state of our parser instance."""


That's nice, but our script is back to a _noop_. So let's implement what we just defined.

    
    class ItemListParser(sax.ContentHandler):
        value_names = (u"boolValue",
            u"floatValue",
            u"intValue",
            u"stringValue", )
        def startDocument(self):
            """We don't need anything special when the document starts."""
        def endDocument(self):
            """We don't need anything special when the document ends."""
        def startElement(self, name, attrs):
            """Save the state depending on the element encountered. Also save the
    data that is useful to us."""
            self._date_time = False
            self._get_characters = False
            value_names = (u"boolValue",
                u"floatValue",
                u"intValue",
                u"stringValue", )
    
            if name == "item":
                self.host_name = attrs.getValue("hostName")
                self.item_name = attrs.getValue("itemName")
            elif name == "dateRecorded":
                self._date_time = True
            elif name in ItemListParser.value_names:
                self._get_characters = True
        def endElement(self, name):
            """Clear the state depending on the element encountered, possibly create an instance of the desired object."""
            if name == "item":
                # we are at the end of an item and now we should be able to
                # construct a new item from the values we saved earlier
                pass
            elif name == "dateRecorded":
                # reset the state
                self._date_time = False
            elif name in ItemListParser.value_names:
                # reset the state
                self._get_characters = False
        def characters(self, content):
            """Save the characters encountered to a helper variable depending on
    the state of our parser instance."""
            try:
                if self._get_characters is True:
                    # yes we are interested in the content here
                    self.value = content
                elif self._date_time is True:
                    self.date_time = content
            except AttributeError, e:
                # if we don't know about self._get_characters or self._date_time yet: don't care
                emit(e)


Now we are all good to go, but still we don't have anything done to our _Item_ class that holds the data we encountered. Let's change that and at least create a single _Item_ that we can print. To do that just modify the endelement method to look like the following:

    
        def endElement(self, name):
            """Clear the state depending on the element encountered,
               possibly create an instance of the desired object."""
            if name == "item":
                # we are at the end of an item and now we should be able to
                # construct a new item from the values we saved earlier
                try:
                    emit(Item(self.host_name,
                        self.item_name,
                        self.date_time,
                        self.value))
                except AttributeError, e:
                    # we may not really now about all the stuff we need by now...
                    pass
            elif name == "dateRecorded":
                # reset the state
                self._date_time = False
            elif name in ItemListParser.value_names:
                # reset the state
                self._get_characters = False


If we now call our python script with a file that contains our sample XML you should get the following output:

    
    $ python itemlistparser.py sampleData.xml
    <: "host1.example.com" "boolean item" "2000-08-13" "true">
    <: "host1.example.com" "float item" "2001-08-13" "1.2">
    <: "host1.example.com" "int item without time" "2002-08-13" "12">
    <: "host1.example.com" "string item without time" "2003-08-13" "foo">
