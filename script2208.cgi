#!/usr/bin/python3

import cgi
formdata = cgi.FieldStorage()
lname = formdata.getfirst('lname', '')
fname = formdata.getfirst('fname', '')
age = formdata.getfirst('age', '')
comment = formdata.getfirst('comment', '')

print('Content-Type: text/html')
print('')
print('''<!DOCTYPE html>
<html>
<head>
<title>Form Results</title>
</head>
<body>
<h2>Here are the results from your survey</h2>
<br />
<table border=1>''')

print('<tr><th>Name</th><td>', fname, lname, '</td></tr>')
print('<tr><th>Age Range</th><td>', age, '</td></tr>')
print('<tr><th>Hobbies</th><td>')
for item in formdata.getlist('hobbies'):
    print(item)
print('</td></tr>')
print('<tr><th>Comments</th><td>', comment, '</td></tr>')
print('</table>')
print('</body>')
print('</html>')
