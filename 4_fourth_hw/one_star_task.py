"""
* you have html page markup, convert it to structure [('google', 'www.google.com', 'Google'),
('facebook', 'http://facebook.com/dign-in', ' Facebook'), ('amazon', 'amazon.com', 'Amazon')]
using only regular expressions. The first element of the tuple is the id of the container the link is in, the second is
the link, and the third is the text of the link
"""
import re

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>
"""

my_list = re.findall(r'"(.*)"\W+\w\W\w+\W+(.*)"\W+(.*)', html_page)

print(my_list)
