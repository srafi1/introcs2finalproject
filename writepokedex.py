def getids():
    try:
        idfile = open('data/csv/pokemon_species.csv', 'rU')
        s = idfile.read()
    except:
        return {}
    s = s.split('\n')
    s = s[1:-1]
    ids = {}
    for i in s:
        i = i.split(',')
        ids[i[0]] = i[1]
    return ids

def gettypes():
    try:
        typefile = open('data/csv/types.csv', 'rU')
        s= typefile.read()
    except:
        return {}
    s = s.split('\n')
    s = s[1:-3]
    d = {}
    for i in s:
        i = i.split(',')
        d[i[0]] = i[1]
    return d

def idtotype(li):
    types = gettypes()
    out = []
    for i in li:
        out.append(types[i])
    return out

def getpoketypes():
    try:
        typefile = open('data/csv/pokemon_types.csv', 'rU')
        s = typefile.read()
    except:
        return {}
    s = s.split('\n')
    last = s.index('10001,14,1')
    s = s[1:last]
    d = {}
    for i in s:
        i = i.split(',')
        if i[0] in d:
            d[i[0]] = d[i[0]] + [i[1]]
        else:
            d[i[0]] = [i[1]]
    for i in d:
        d[i] = idtotype(d[i])
    return d

def getstats():
    try:
        f = open('data/csv/pokemon_stats.csv', 'rU')
        s = f.read()
    except:
        return {}
    s = s.split('\n')
    last = s.index('10001,1,50,0')
    s = s[1:-1]
    d = {}
    for i in s:
        i = i.split(',')
        if i[0] in d:
            d[i[0]] = d[i[0]] + [i[2]]
        else:
            d[i[0]] = [i[2]]
    return d

def getpokeinfo():
    ids = getids()
    poketypes = getpoketypes()
    stats = getstats()

    li = []
    for i in ids:
        poke = []
        poke.append(int(i))
        poke.append(ids[i])
        poke.append(poketypes[i][0])
        if len(poketypes[i]) > 1:
            poke.append(poketypes[i][1])
        else:
            poke.append('')
        poke.append(stats[i][0])
        for j in range(1,6):
            poke.append(stats[i][j])
        li.append(poke)
    li.sort()
    return li

def writedata():
    f = open('poketypes.csv', 'w')
    out = getpokeinfo()
    f.write(str(out[0][0]))
    for i in out[0][1:]:
        f.write(',' + i)
    for i in out[1:]:
        f.write('\n' + str(i[0]))
        for j in i[1:]:
            f.write(',' + j)
    f.close()
    print 'done'
