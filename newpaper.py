#!/usr/bin/python

import os
import sys
import os.path
import errno
from datetime import datetime
from string import Template

front_matter = "---\n"\
	"layout: paper\n"\
	"title: ${title}\n"\
	"date: ${date}\n"\
	"---\n\n"

front_matter_data = {
		u"layout": u"paper",
		u"title": None,
		u"date": datetime.now(),
		}
	

def main(args):
	title = u" ".join([arg.decode("utf-8") for arg in args[1:]])
	date = datetime.today()

	front_matter_data[u"title"] = title
	front_matter_data[u"date"] = date.strftime(u"%F")
	papers_dir = u"papers"
	paper_file = u"{}-{}.md".format(
			front_matter_data[u"date"],
			front_matter_data[u"title"].lower().replace(u" ", u"-"),
			)
	paper = os.path.join(papers_dir, paper_file)

	t = Template(front_matter)
	boilerplate = t.safe_substitute(front_matter_data)
	print boilerplate
	try:
		os.makedirs(papers_dir)
	except os.error, err:
		if err.errno == errno.EEXIST:
			pass
		else:
			raise
	try:
		f = os.open(paper.encode("utf-8"), os.O_CREAT | os.O_WRONLY)
		os.write(f, boilerplate)
		os.fsync(f)
		os.close(f)
	except OSError, err:
		raise
	print "Run vim {}".format(paper)



if __name__ == '__main__':
    main(sys.argv)
