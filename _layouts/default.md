<!DOCTYPE html>
<html>
  <head>
    <meta charset="{{ site.encoding }}">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ page.title }}</title>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <!-- <script src="js/bootstrap.min.js"></script> -->

    <!-- bootstrap -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">

    <!-- Optional theme -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">

    <!-- Latest compiled and minified JavaScript -->
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Pygments css -->
    <link rel="stylesheet" href="/css/syntax.css">

    <!-- site local styles -->
    <link rel="stylesheet" href="/css/site.css">

    <!-- Publisher Information -->
    <link href="https://plus.google.com/106689595059572911333" rel="publisher" />
  </head>
  <body class="container">
    <header class="container-fluid">
    <h1 class="page-header"><a href="{{ site.baseurl }}" class="navbar-brand">{{ site.name }}</a> <small>{{ site.tagline }}</small></h1>
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
      <ul class="nav navbar-nav">
        <li><a href="/">home</a></li>
        <li><a href="/blog/">blog</a></li>
        <li><a href="/about/">about</a></li>
      </ul>
    </nav>
    </header>
    <section>
    {{ content }}
    </section>
    <footer class="container-fluid">
      <nav class="navbar navbar-default navbar-fixed-bottom">
        <ul class="nav navbar-nav">
          <li><a href="mailto:martin@marcher.name">martin@marcher.name</a></li>
          <li><a href="https://github.com/serverhorror">github.com/serverhorror</a></li>
          <li><a href="https://twitter.com/serverhorror">twitter.com/serverhorror</a></li>
          <li><a href="//plus.google.com/106689595059572911333?rel=author">Google+</a></li>
        </ul>
      </nav>
    </footer>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
      ga('create', 'UA-23535287-5', 'serverhorror.com');
      ga('send', 'pageview');
    
    </script>
  </body>
{% comment %} vim: set ts=2 sts=2 fenc=utf-8 expandtab: {% endcomment %}
</html>
