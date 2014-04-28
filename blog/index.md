---
layout: default
---
<ul class="container-fluid list-unstyled">
  {% for post in site.posts %}
    <li>
      <date pubdate time="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_string }} &raquo; <a href="{{ post.url }}">{{ post.title }}</a></date>
    </li>
  {% endfor %}
</ul>
<!-- vim: set ts=2 sts=2 fenc=utf-8 expandtab: -->
