---
layout: default
---
<article itemscope itemtype="http://schema.org/Article" pubdate="{{ page.date | date_to_xmlschema }}" class="container-fluid">
  <h1 itemprop="name">{{ page.title }}</h1>
  <time itemprop="datePublished" class="meta" content="{{ page.date | date_to_xmlschema }}" datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date_to_string }}</time>
  {{ content }}
  {% if page.author != nil %}
  <address rel="author">
    <a href="//twitter.com/serverhorror">
      <span  itemprop="author" itemscope itemtype="http://schema.org/Person">
        <span itemprop="name">{{ page.author }}</span>
      </span>
    </a>
  </address>
  {% endif %}
  {% comment %}
  {% endcomment %}
</article>
<ul class="pager">
  <li class="previous"><a href="{{ site.baseurl }}{{ page.previous.url }}" rel="previous">&larr; Previous</a></li>
  <li class="next"><a href="{{ site.baseurl }}{{ page.next.url }}" rel="next">Next &rarr;</a></li>
</ul>
{% comment %} vim: set ts=2 sts=2 fenc=utf-8 expandtab: {% endcomment %}
