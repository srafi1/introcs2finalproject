#! /usr/bin/python
import cgi
import cgitb
cgitb.enable()

content = 'Content-type: text/html\n\n'
top = '<html><body>'
bottom = '</body></html>'
print content + top + bottom
