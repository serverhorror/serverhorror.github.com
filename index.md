---
layout: default
---
<ul class="container-fluid list-unstyled">
  {% for post in site.posts %}
    <li>
      <time pubdate time="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_string }} <a class="fa fa-angle-double-right" href="{{ post.url }}">{{ post.title }}</a></time>
    </li>
  {% endfor %}
</ul>

<!-- vim: set ts=2 sts=2 fenc=utf-8 expandtab: -->
