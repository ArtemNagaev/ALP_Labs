#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
name = form.getfirst("user_name", "Аноним")
name = html.escape(name)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка введенных данных</title>
        </head>
        <body>""")

print("<p>Здравствуйте, {}</p>".format(name))
print("<a href='/'>Вернуться на главную страницу</a>")

print("""</body>
        </html>""")
