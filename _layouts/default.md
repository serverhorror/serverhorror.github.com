<!DOCTYPE html>
<html>
  <head>
    <meta charset="{{ site.encoding }}">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ page.title }}</title>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script async src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <!-- <script async src="js/bootstrap.min.js"></script> -->

    <!-- bootstrap -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">

    <!-- Optional theme -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">

    <!-- Latest compiled and minified JavaScript -->
    <script async src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script async src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script async src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- FontAwesome -->
    <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">

    <!-- Source Code Pro -->
    <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro' rel='stylesheet' type='text/css'>

    <!-- Github Projects CSS -->
    {% comment %}
    {% endcomment %}
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/jquery-github/assets/base.css">

    <!-- Pygments css -->
    <link rel="stylesheet" href="{{ site.baseurl }}/css/syntax.css">

    <!-- site local styles -->
    <link rel="stylesheet" href="{{ site.baseurl }}/css/site.css">

    <!-- Google Publisher Information -->
    <link href="https://plus.google.com/106689595059572911333" rel="publisher" />

    <!-- Twitter Card -->
    {% comment %}
    {% endcomment %}
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Server/!Horror!">
    <meta name="twitter:description" content="I have a magnet and I don't mind using it!">


    {% comment %}
    <!-- Facebook Open Graph -->
    {% endcomment %}
    <!-- Feeds -->
    <link rel="alternate" type="application/atom+xml" title="{{ site.name }} ATOM Feed" href="{{ site.baseurl }}/atom.xml">
    <link rel="sitemap" type="application/xml" title="{{ site.name }} Sitemap" href="{{ site.baseurl}}/sitemap.xml" />


  </head>
  <body class="container">
    <header class="container-fluid">
    <h1 class="page-header"><a href="{{ site.baseurl }}" class="navbar-brand">{{ site.name }}</a> <small>{{ site.tagline }}</small></h1>
    <nav class="navbar navbar-default navbar-static-top" role="navigation">
      <ul class="nav navbar-nav">
        <li><a class="fa fa-home" href="{{ site.baseurl }}/">home</a></li>
        {% comment %}
        {% endcomment %}
        <li><a href="{{ site.baseurl }}/blog/">blog</a></li>
        <li><a href="{{ site.baseurl }}/about/">about</a></li>
        <li><a class="fa fa-github" href="{{ site.baseurl }}/projects/">projects</a></li>
      </ul>
    </nav>
    </header>
    <section class="container">
    {{ content }}
    </section>
    <footer class="container-fluid">
      <nav class="navbar navbar-default navbar-static-bottom">
        <ul class="nav navbar-nav">
          <li><a  class="fa fa-envelope" href="mailto:martin@marcher.name">martin@marcher.name</a></li>
          {% comment %}
          <li><a class="fa fa-github" href="//github.com/serverhorror">github.com/serverhorror</a></li>
          {% endcomment %}
          <li><a class="fa fa-twitter" href="//twitter.com/serverhorror">twitter.com/serverhorror</a></li>
          <li><a class="fa fa-google-plus" href="//plus.google.com/106689595059572911333?rel=author">Google+</a></li>
          <li><a class="fa fa-xing" href="//www.xing.com/go/invite/7047758">Xing</a></li>
          <li><a class="fa fa-linkedin-square" href="//de.linkedin.com/in/martinmarcher">LinkedIn</a></li>
        </ul>
      </nav>
    </footer>
    <p class="well">Generated: {{ site.time }}</p>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
      ga('create', 'UA-23535287-5', 'serverhorror.com');
      ga('require', 'displayfeatures');
      ga('send', 'pageview');
    
    </script>
  </body>
{% comment %} vim: set ts=2 sts=2 fenc=utf-8 expandtab: {% endcomment %}
</html>
