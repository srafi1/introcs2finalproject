#! /usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
if 'x' not in form or 'y' not in form:
	x = 11
	y = 6
else:
	x = int(form['x'].value)
	y = int(form['y'].value)
if 'encounters' in form:
	e = form['encounters'].value
	e = e.split(',')
	enc = []
	for i in e:
		if not i in enc:
			enc.append(i)
	newenc = enc[0]
	for i in enc[1:]:
		newenc += ',' + i

content = 'Content-type: text/html\n\n'
top_html = '''
<html>
<head>
<link rel=icon href=../img/favicon.ico>
<title>Explore</title>
<style type=text/css>
body {
font-family: Arial;
font-size: 150%
}
td, th {
border: 2px solid black;
}
a:hover {
color: #000099;
}
td {
border: 2px solid black;
}
table {
border-collapse: collapse;
}
</style>
<script type=text/javascript src=explore.js></script>
</head>
<body background=../img/pokeworld.png onload=start()>
<center>
<a href=..>
<img src=../img/logo.png width=600px> </a>
<div id=content style="background:#ccccff;width:900px;padding:5px;">
<center>
Explore <br>
'''
bottom_html = '</center></div></body></html>'
print content + top_html
if 'encounters' in form:
	try:
		f = open('../pokedex.csv', 'rU')
		s = f.read()
	except:
		s = ''
	s = s.split('\n')
	info = 'Encountered Pok&eacutemon<br><table><th>Dex #</th><th>Image</th><th>Name</th><th>Type 1</th><th>Type 2</th>'
	for i in enc:
		if not i.isdigit():
			continue
		info += '<tr><td>#' + i + '</td>'
		info += '<td><img src=../img/pokemon/' + i + '.png height=100px></td>'
		data = s[int(i)].split(',')
		info += '<td><a href=pokedex.py?name_dex=' + i + '&x=' + str(x) + '&y=' + str(y) + '&encounters=' + newenc + '>'  + data[1].capitalize() + '</a></td>'
		info += '<td><img src=../img/' + data[2] + '.png height=20px></td>'
		if data[3] != '':
			info += '<td><img src=../img/' + data[3] + '.png height=20px></td></tr>'
		else:
			info += '<td></td>'
	info += '</table'
else:
	info = '''
Walk around using the arrow keys. Go to any of the four sections to encounter different Pok&eacute;mon based on the environment and types. Encountered Pok&eacute;mon will appear here.<br>
'''
content = '''
<canvas id=rpg width=840px height=490px style="border:1px solid #000000"></canvas><br>
<div width=840>
<p id=info>''' + info + '''
</p>
</div>
<img src=../img/rpgsprite.png id=sprite width=0 height=0>
<img src=../img/watersprite.png id=watersprite width=0 height=0>
<img src=../img/rpg.png id=map width=0 height=0>
<p id=xcoord hidden>''' + str(x) + '''</p>
<p id=ycoord hidden>''' + str(y) + '''</p>
'''
if 'encounters' in form:
	content += '<p id=encounters hidden>' + newenc + '</p>'
else:
	content += '<p id=encounters hidden></p>'
print content + bottom_html
