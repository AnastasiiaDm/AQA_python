"""
** you have the same page markup file, but you need to give out a structure in which not the whole link but only the
domain name: [('google', 'google.com', 'Google'), ('facebook', 'facebook. com', 'Facebook'),
('amazon', 'amazon.com', 'Amazon')]
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

my_list = re.findall(r'"(.*)"\W+\w\W\w+(?:\W+www|\W+http|)\W+(.*com)\S+\W+(.*)', html_page)

print(my_list)
