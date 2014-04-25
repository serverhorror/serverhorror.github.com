<!DOCTYPE html>
<html>
    <head>
        <meta charset="{{ site.encoding }}">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>{{ page.title }}</title>
        <meta name="viewport" content="width=device-width">

        <!-- syntax highlighting CSS -->
        <link rel="stylesheet" href="/css/syntax.css">

        <!-- Custom CSS -->
        <link rel="stylesheet" href="/css/main.css">

        <!-- Publisher Information -->
        <link href="https://plus.google.com/106689595059572911333" rel="publisher" />

    </head>
    <body>

        <section class="site">
          {% include header.html %}
          {{ content }}
          {% include footer.html %}
        </section>

        <script>
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        
          ga('create', 'UA-23535287-5', 'serverhorror.com');
          ga('send', 'pageview');
        
        </script>
    </body>
<!-- vim: set ts=4 sts=4 fenc=utf-8 expandtab: -->
</html>
