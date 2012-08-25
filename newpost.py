#!/usr/bin/python

import os
import sys
import os.path
import errno
from datetime import datetime
from string import Template

front_matter = "---\n"\
	"layout: post\n"\
	"title: ${title}\n"\
	"date: ${date}\n"\
	"---\n\n"

front_matter_data = {
		u"layout": u"post",
		u"title": None,
		u"date": datetime.now(),
		}
	

def main(args):
	title = u" ".join([arg.decode("utf-8") for arg in args[1:]])
	date = datetime.today()

	front_matter_data[u"title"] = title
	front_matter_data[u"date"] = date
	posts_dir = u"_posts"
	post_file = u"{}-{}.md".format(
			front_matter_data[u"date"],
			front_matter_data[u"title"].lower().replace(u" ", u"-"),
			)
	post = os.path.join(posts_dir, post_file)

	t = Template(front_matter)
	boilerplate = t.safe_substitute(front_matter_data)
	print boilerplate
	try:
		f = os.open(post.encode("utf-8"), os.O_CREAT | os.O_WRONLY)
		os.write(f, boilerplate)
		os.fsync(f)
		os.close(f)
	except OSError, err:
		raise
	print "Run vim {}".format(post)



if __name__ == '__main__':
    main(sys.argv)
