---
layout: default
---
<article pubdate="{{ page.date | date_to_xmlschema }}" class="container-fluid">
  <h2>{{ page.title }}</h2>
  <time class="meta" datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date_to_string }}</time>
  {{ content }}
  {% comment %}
  {% if page.author %}
  <address rel="author">Author: <a href="//twitter.com/serverhorror">{{ page.author }}</a></address>
  {% endif %}
  {% endcomment %}
</article>
<ul class="pager">
  <li class="previous"><a href="{{ site.baseurl }}{{ page.previous.url }}" rel="previous">&larr; Previous</a></li>
  <li class="next"><a href="{{ site.baseurl }}{{ page.next.url }}" rel="next">Next &rarr;</a></li>
</ul>
{% comment %} vim: set ts=2 sts=2 fenc=utf-8 expandtab: {% endcomment %}
