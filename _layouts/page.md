---
layout: default
---
<article class="container-fluid">
  <h2>{{ page.title }}</h2>
  {% if page.date %}<date datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date_to_string }}</date>{% endif %}
  {{ content }}
</article>
<!-- vim: set ts=2 sts=2 fenc=utf-8 expandtab: -->
