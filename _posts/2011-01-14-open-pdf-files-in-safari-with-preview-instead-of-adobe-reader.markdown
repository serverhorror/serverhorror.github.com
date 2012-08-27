---
comments: true
date: 2011-01-14 18:57:37
layout: post
slug: open-pdf-files-in-safari-with-preview-instead-of-adobe-reader
title: Open PDF files in Safari with Preview instead of Adobe Reader
wordpress_id: 909
tags:
- adobe
- browser
- os x
- osx
- pdf
- preview
- safari
- snow leopard
---

I recently installed Adobe Reader to have it available on my OS X (Snow Leopard) installation.

From that point on Safari insisted on opening PDF files in the browser with Adobe Reader instead of Preview.app.



	
  1. Changing the way PDF files are opened in Finder didn't help

	
  2. Scanning Safari Preferences didn't help

	
  3. Scanning Adobe Prefences revealed an option but I wasn't able to uncheck it. ("Preferences" -> "Internet" -> "Display PDF in browser using:" - in case you are searching


To "switch back" delete (or move) the file "/Library/Internet Plug-Ins/AdobePDFViewer.plugin". The resulting preferences from Adobe Reader are shown below. Also now you have Preview.app back in Safari when opening PDF files.

[![](http://serverhorror.files.wordpress.com/2011/01/adobereaderprefs.png)](http://serverhorror.files.wordpress.com/2011/01/adobereaderprefs.png)To be able to switch around easily I recommend you simply move the file to a convenient location. If you need Safari to open PDF files with Adobe Reader again just move "AdobePDFViewer.plugin" back to "/Library/Internet Plug-Ins/" and restart Safari. The same approach should work if you move it to "~/Library/Internet Plug-Ins/" - though I haven't tested that and right now I am too lazy to do that...
