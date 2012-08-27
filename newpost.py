#!/usr/bin/python

import os
import sys
import os.path
import errno
import subprocess
import unicodedata
import re
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

def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.


    Honestly stolen from:

        * https://github.com/django/django/blob/master/django/utils/text.py
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


def main(args):
    title = u" ".join([arg.decode("utf-8") for arg in args[1:]])
    date = datetime.today()


    front_matter_data[u"title"] = title
    front_matter_data[u"date"] = date.strftime(u'%F')
    posts_dir = u"_posts"
    post_file = u"{}-{}".format(
            front_matter_data[u"date"],
            slugify(front_matter_data[u"title"], ),
            )
    post_file = "{}.md".format(post_file)
    post = os.path.abspath(os.path.join(posts_dir, post_file))

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
    subprocess.call(["git", "add", post])
    editor = os.getenv("EDITOR", "vim")
    os.execlp(editor, editor, "{}".format(post))



if __name__ == '__main__':
    main(sys.argv)

# vim: set ts=4 sts=4 fenc=utf-8 expandtab :
