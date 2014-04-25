---
layout: default
---
<article class="post">
<h2>{{ page.title }}</h2>
<time class="meta" datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date_to_string }}</time>
{{ content }}
</article>

<!-- vim: set ts=4 sts=4 fenc=utf-8 expandtab: -->
