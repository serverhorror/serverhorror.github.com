---
layout: default
title: Server!/Horror!
---
<div id="carousel-landing-page" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-landing-page" class="active"></li>
  </ol>
  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    <div class="item container navbar-inverse active">
      <img class="landing" src="{{ site.baseurl}}/assets/load-graph.png" alt="General System Load" />
      <img class="landing" src="{{ site.baseurl}}/assets/java-heap-memory-graph.png" alt="Java Heap Memory" />
      <div class="carousel-caption">
        <h1>Better Data</h1>
        <ul class="list-unstyled">
          <li >Providing better service with graphing solutions that are maintainable and usable by everyone!</li>
          <li><a href="mailto:{{ site.business_contact }}" type="button" class="btn btn-default btn-lg">Get in touch...</a></li>
        </ul>
        
      </div>
    </div>
  </div>
  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-landing-page" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="#carousel-landing-page" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>
</div>
{% comment %} vim: set ts=2 sts=2 fenc=utf-8 expandtab: {% endcomment %}
