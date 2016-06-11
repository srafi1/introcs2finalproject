#! /usr/bin/python
import cgi
import cgitb
import random
cgitb.enable()

form = cgi.FieldStorage()
x = form['x'].value
y = form['y'].value
if 'encounters' in form:
	enc = form['encounters'].value + ','
else:
	enc = ''
area = form['area'].value

if area == 'grass':
	types = ['grass', 'normal', 'fighting', 'flying', 'poison', 'electric', 'fairy', 'psychic', 'bug']
elif area == 'desert':
	types = ['ground', 'rock', 'steel', 'fire', 'dragon']
elif area == 'water':
	types = ['water', 'ice', 'flying']
else:
	types = []
	
try:
	f = open('../pokedex.csv', 'rU')
	s = f.read()
except:
	s = ''
s = s.split('\n')[1:]
out = []
for i in s:
	i = i.split(',')
	if i[2] in types or area == 'random':
		out.append(i)
rand = random.randint(0, len(out) - 1)
poke = out[rand]

enc += poke[0]
if random.randint(0, 50) <= 1 and int(poke[0]) <= 649:
	shiny = True
else:
	shiny = False
if shiny:
	info = '<img src=../img/pokemon/shiny/' + poke[0] + '.png height=300px><br>'
else:
	info = '<img src=../img/pokemon/' + poke[0] + '.png height=300px><br>'
info += '<a href=pokedex.py?name_dex=' + poke[0] + '&x=' + x + '&y=' + y + '&encounters=' + enc + '>Go to pokedex listing of ' + poke[1].capitalize() + '</a> (or press O) <br>'
info += '<a href=explore.py?x=' + x + '&y=' + y + '&encounters=' + enc + '>Find more Pok&eacute;mon</a> (or press P)'

content = 'Content-type: text/html\n\n'
top_html = '''
<html>
<head>
<link rel=icon href=../img/favicon.ico>
<title>Encounter</title>
<style type=text/css>
body {
font-family: Arial;
font-size: 150%
}
a:hover {
color: #000099;
}
</style>
<script type=text/javascript>
window.onkeydown = function(e) {
var key = e.keyCode;
if (key == 79) window.location = "pokedex.py?name_dex=''' + poke[0] + '&x=' + x + '&y=' + y + '&encounters=' + enc + '''";
else if (key == 80) window.location = "explore.py?x=''' + x + '&y=' + y + '&encounters=' + enc + '''";
}
</script>
</head>
<body background=../img/pokeworld.png>
<center>
<a href=..>
<img src=../img/logo.png width=600px> </a>
<div id=content style="background:#ccccff;width:900px;padding:5px;">
<center>
'''
if shiny:
	top_html += 'Oooo shiny!!!<br>'
else:
	top_html += "You've encountered a Pok&eacute;mon! <br>"
bottom_html = '</center></div></body></html>'
print content + top_html + info + bottom_html
