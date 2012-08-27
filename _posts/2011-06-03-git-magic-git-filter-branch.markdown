---
comments: true
date: 2011-06-03 18:14:18
layout: post
slug: git-magic-git-filter-branch
title: Git Magic (git filter-branch)
wordpress_id: 1285
tags:
- Apache Subversion
- Author
- git
- Literature
- Revision control
- Source code
- Tools
---

Rewrite all commits in `git` to a new author:

[sourcecode]
git filter-branch -f --env-filter '\
    GIT_AUTHOR_EMAIL=author@example.invalid; \
    export GIT_AUTHOR_EMAIL; \
    GIT_AUTHOR_NAME="New Author"; \
    export GIT_AUTHOR_NAME'
[/sourcecode]
