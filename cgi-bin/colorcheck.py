#!/usr/local/bin/python3
import cgi
import os

form = cgi.FieldStorage()
color = form.getvalue("color")
path = "/Users/l2/Dev/learning/foundation/color-check/cgi-bin/colors.txt"

colordoc = open(path, "r")
content = colordoc.read()

found = False
if (color.lower() in content):
    found = True

colordoc.close()

if found:
    output = "Awesome! " + color + " is a nice color! 💯"
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
  </html>""".format(output, color, output)

print(html)
