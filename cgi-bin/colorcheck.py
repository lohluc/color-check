#!/usr/local/bin/python3
import cgi
import os
from colors import color_info

form = cgi.FieldStorage()
form_input = form.getvalue("color")

found = False
if (form_input.lower() in color_info) or (form_input.lower() in color_info.values()):
    found = True

if found:
    for key, value in color_info.items():
        output = "What a beautiful color! 🤩 " + color_info[form_input].capitalize()
else:
    output = "Oh no... I don't know this color! 🥺" 


html = """
<!DOCTYPE html>
  <html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8" />
        <title>{}</title>
        <link rel="stylesheet" href="../style.css">
    </head>
    <body>
        <div class="container">
            <div class="icon">🎨</div>
            <div class="color" style="background-color: {}"></div>
            <h1>{}</h1>
            <a class="button-again" href="/index.html">Try it again</a>
        </div>
        <div class="footer">
                <p>Made by 
                    <a href="https://twitter.com/lohluc" target="_blank">L2</a>
                    during the foundation semester at
                    <a href="https://code.berlin" target="_blank">CODE</a>
                </p>
        </div>
    </body> 
  </html>""".format(output, form_input, output)

print(html)
