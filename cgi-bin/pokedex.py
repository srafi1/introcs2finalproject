#! /usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()

form = cgi.FieldStorage()
content = 'Content-type: text/html\n\n'
if 'all' in form:
     title = 'All Pok&eacute;mon'
     process = 'all'
     data = ''
elif 'name_dex' in form:
     title = 'Listing for ' + form['name_dex'].value
     process = 'name_dex'
     data = form['name_dex'].value
elif 'type' in form:
     title = 'All ' + form['type'].value + ' type Pok&eacute;mon'
     process = 'type'
     data = form['type'].value
elif 'stat' in form and 'order' in form:
     title = 'All Pok&eacute;mon by ' + form['stat'].value
     process = 'stat'
     data = form['stat'].value
     if form['order'].value == 'top':
          from_top = True
     else:
          from_top = False
else:
     title = 'Error'
     process = 'error'
top_html = '''
<html>
<head>
<link rel=icon href=../img/favicon.ico>
<title>''' + title + '''</title>
<style type=text/css>
div {
width: 90%;
padding: 5px;
}
body {
font-family: Arial;
font-size: 150%
}
td, th {
border: 2px solid black;
}
table {
border-collapse: collapse;
}
a:hover {
color: #000099;
}
</style>
</head>
<body background=../img/pokeworld.png onload=changeBackground()>
<center>
<a href=..>
<img src=../img/logo.png width=600px> </a>
<div id=content style="background:#ccccff">
'''
bottom_html = '</table><p><a href=../pokedex.html>Back to pokedex query</a></p></div></center></body></html>'
print content, top_html

def printhead():
     th = '<tr>'
     th += '<td>Dex #</td>'
     th += '<td>Pok&eacute;mon name</td>'
     th += '<td>Type 1</td>'
     th += '<td>Type 2</td>'
     th += '<td>Base HP</td>'
     th += '<td>Base Attack</td>'
     th += '<td>Base Defense</td>'
     th += '<td>Base Sp. Attack</td>'
     th += '<td>Base Sp. Defense</td>'
     th += '<td>Base Speed</td>'
     th += '</tr>'
     print th

def printlisting(l):
     out = ''
     out += '<tr><td>#' + l[0] + '</td>'
     out += '<td><a href=pokedex.py?name_dex=' + l[1] + '>' + l[1].capitalize() + '</td>'
     out += '<td><img src=../img/' + l[2] + '.png height=20px></td>'
     if l[3] == '':
          out += '<td></td>'
     else:
          out += '<td><img src=../img/' + l[3] + '.png height=20px></td>'
     out += '<td>' + l[4] + '</td>'
     out += '<td>' + l[5] + '</td>'
     out += '<td>' + l[6] + '</td>'
     out += '<td>' + l[7] + '</td>'
     out += '<td>' + l[8] + '</td>'
     out += '<td>' + l[9] + '</td>'
     out += '</tr>'
     print out

def doall():
     try:
          cwd = os.getcwd()
          updir = cwd[:cwd.rfind('/')]
          f = open(updir + '/pokedex.csv')
          s = f.read()
     except:
          doerror()
          return
     print 'All Pok&eacute;mon <br><table style="border-collapse:collapse" width=80%>'
     printhead()
     s = s.split('\n')[1:]
     for i in s:
          printlisting(i.split(','))

def dotype():
     try:
          cwd = os.getcwd()
          updir = cwd[:cwd.rfind('/')]
          f = open(updir + '/pokedex.csv')
          s = f.read()
     except:
          doerror()
          return
     print 'All ' + data + ' type Pok&eacute;mon <br><table style="border-collapse:collapse" width=80%>'
     printhead()
     s = s.split('\n')[1:]
     li = []
     for i in s:
          i = i.split(',')
          if data == i[2] or data == i[3]:
               li.append(i)
     for i in li:
          printlisting(i)

def dostat():
     try:
          cwd = os.getcwd()
          updir = cwd[:cwd.rfind('/')]
          f = open(updir + '/pokedex.csv')
          s = f.read()
     except:
          doerror()
          return
     print 'Pok&eacute;mon by ' + data + ' stat<br><table style="border-collapse:collapse" width=80%'
     printhead()
     s = s.split('\n')[1:]
     tosort = []
     if data == 'hp':
          statindex = 4
     if data == 'attack':
          statindex = 5
     if data == 'defense':
          statindex = 6
     if data == 'spattack':
          statindex = 7
     if data == 'spdefense':
          statindex = 8
     if data == 'speed':
          statindex = 9
     for i in s:
          i = i.split(',')
          next = [int(i[statindex])] + i
          tosort.append(next)
     tosort.sort()
     if from_top:
          tosort = tosort[::-1]
     for i in range(len(tosort)):
          tosort[i] = tosort[i][1:]
          printlisting(tosort[i])

def printpokeinfo(l, d):
	out = l[1].capitalize() + '''
	<table style="background:#DDDDFF" width=80%>
	 <tr>
		 <td height=300px width=300px><img src=../img/pokemon/''' + l[0] + '''.png height=300px width=300px></td>
		 <td height=300px>
			 <table height=100% width=100%>
			 <tr>
				 <th colspan=4>Species</td>
			 </tr>
			 <tr>
				 <td colspan=4>''' + l[1].capitalize() + '''</td>
			 </tr>
			 <tr>
				 <th>Type 1</td>
				 <th>Type 2</td>
				 <th>Height</td>
				 <th>Weight</td>
			 </tr>
			  <tr>
				  <td><img src=../img/''' + l[2] + '''.png height=20px></td>
				  <td>'''
	if l[3] != '':
		out += '<img src=../img/' + l[3] + '.png height=20px>'
	out += '''</td>
				  <td>''' + l[10][:-1] + '.' + l[10][-1] + '''m</td>
				  <td>''' + l[11][:-1] + '.' + l[10][-1] +  '''kg</td>
			  </tr>
			  
			  <tr>
				  <th colspan=4>
					  Description
				  </td>
			  </tr>
			   <tr>
				   <td colspan=4>
					   ''' + d + ''' 
				   </td>
			   </tr>
			 </table>
		 </td>
	 </tr>
		<tr>
			<td colspan=2>
			<table width=100%>
				<tr>
					<th colspan=6>Stats</th>
				</tr>
				<tr>
					<th>HP</td>
					<th>Attack</td>
					<th>Defense</td>
					<th>Special Attack</td>
					<th>Special Defense</td>
					<th>Speed</td>
				</tr>
				<tr>
					<td>''' + l[4] + '''</td>
					<td>''' + l[5] + '''</td>
					<td>''' + l[6] + '''</td>
					<td>''' + l[7] + '''</td>
					<td>''' + l[8] + '''</td>
					<td>''' + l[9] + '''</td>
				</tr>
			</table>
		 </td>
		</tr>
	'''
	print out

def doname_dex():
     try:
          cwd = os.getcwd()
          updir = cwd[:cwd.rfind('/')]
          f = open(updir + '/pokedex.csv')
          s = f.read()
     except:
          doerror()
          return
     s = s.split('\n')
     data = data = form['name_dex'].value
     if data.replace('-', '').replace('.', '').isdigit():
          try:
          	data = int(float(data))
          except:
			print 'You entered: ', form['name_dex'].value, '<br>'
		  	print 'Please enter a number between 1 and 721 <table hidden>'
			return
          if not (data <= 721 and data > 0):
          	print 'You entered: ', form['name_dex'].value, '<br>'
          	print 'Please enter a number between 1 and 721 <table hidden>'
          	return
          poke = s[data].split(',') # change to getting all data leter on
     else:
     	out = []
	data = data.strip()
     	for i in s[1:]:
     		i = i.split(',')
     		if data.lower() == i[1][:len(data)]: #process for each
     			if data.lower() == i[1]:
     				out = [i]
     				break
     			out.append(i)
     	for i in s[1:]:
			if data.lower() == i[1]:
				out = [i]
				break
			i = i.split(',')
			if data.lower() in i[1] and not i in out: #process for each
				out.append(i)
	for i in s[1:]:
                i = i.split(',')
                if data.lower() == i[1]:
                        out = [i]
                        break
     	if len(out) == 1:
     		poke = out[0]
     	elif len(out) == 0:
     		print 'No Pok&eacute;mon match the phrase: ' + data + '<table hidden>'
     		return
     	else:
     		print 'Pok&eacute;mon with "' + data + '" in their name<table style="border-collapse:collapse" width=80%'
     		printhead()
     		for i in out:
     			printlisting(i)
     		return
     f = open('../descriptions.csv', 'rU')
     s = f.read()
     s = s.split('\n')
     desc = s[int(poke[0]) - 1].split('"')[1]
     mainType = poke[2]
     colors = {'normal': '#A8A77A','fighting': '#C22E28','flying': '#A98FF3','poison': '#A33EA1','ground': '#E2BF65','rock': '#B6A136','bug': '#A6B91A','ghost': '#735797','steel': '#B7B7CE','fire': '#EE8130','water': '#6390F0','grass': '#7AC74C','electric': '#F7D02C','psychic': '#F95587','ice': '#96D9D6','dragon': '#6F35FC','dark': '#302726','fairy': '#D685AD'}
     color = colors[mainType]
     print '''
     <script type=text/javascript>
     function changeBackground() {
     	var div = document.getElementById('content');
     	var color = "''' + color + '''"
		div.style.background = color;
		if (color == "#302726") div.style.color = "#FFFFFF";
	 }
     </script>'''
     printpokeinfo(poke, desc)

def doerror():
	print 'Please enter a name or dex number or choose to sort by stat or a type <table hidden>'

if process == 'all':
     doall()
elif process == 'type':
     dotype()
elif process == 'stat':
     dostat()
elif process == 'name_dex':
     doname_dex()
elif process == 'error':
     doerror()
     
if 'encounters' in form:
	enc = form['encounters'].value
	x = form['x'].value
	y = form['y'].value
	bottom_html = '</table><p><a href=../pokedex.html>Back to pokedex query</a><br><a href=explore.py?encounters=' + enc + '&x=' + x + '&y=' + y + '>Back to Explore</a></p></div></center></body></html>'

print bottom_html
