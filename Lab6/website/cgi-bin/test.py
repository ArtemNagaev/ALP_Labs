#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
name = form.getfirst("user_name", "Аноним")
name = html.escape(name)

print("Content-type: text/html\n")
print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <meta http-equiv="Content-Type" content="text/html; charset=CP1251"/>
        <head>
            <title>Обработка введенных данных</title>
        </head>
        <body>""")

print("<p>Здравствуйте, {}</p>".format(name))
print("<a href='/'>Вернуться на главную страницу</a>")

print("""</body>
        </html>""")
