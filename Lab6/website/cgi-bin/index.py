#!/usr/bin/env python3

print("Content-type: text/html")
print()

print('<head> \
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> \
    <title></title> \
    <meta name="keywords" content=""/> \
    <meta name="description" content=""/> \
    <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet"/> \
    <link href="/default.css" rel="stylesheet" type="text/css" media="all"/> \
    <link href="/fonts.css" rel="stylesheet" type="text/css" media="all"/> \
</head>')
print('<body> \
<div id="header-wrapper"> \
    <div id="header" class="container"> \
        <div id="logo"> \
            <h1><span class="fa fa-bolt"></span><a href="/">Лабораторная работа №6</a></h1> \
        </div> \
        <div id="menu"> \
            <ul> \
                <li><a href="/" accesskey="1" title="">Главная</a></li> \
                <li class="current_page_item"><a href="/cgi-bin/index.py" accesskey="2" title="">Информация</a></li> \
            </ul> \
        </div> \
    </div> \
</div> \
<div id="header-featured"> \
    <div id="banner-wrapper"> \
        <div id="banner" class="container"> \
           <h2>Информация о сайте</h2> \
        </div> \
    </div> \
</div> \
<div id="copyright" class="container"> \
    <p>&copy; Лабораторная работа №6. All rights reserved.</p> \
</div> \
</body>')
# </html>
