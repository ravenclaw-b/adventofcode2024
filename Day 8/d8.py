fhandle = open("d8input.txt")
mydict = {}

n = 0
ant = set()
ans = set()

for line in fhandle:
    line = line.strip()
    m = len(line)
    for i in range(m):
        if (line[i] != '.'):
            if (line[i] not in mydict.keys()):
                mydict[line[i]] = [(n, i)]
            else:
                mydict[line[i]].append((n, i))
            ant.add((n, i))
    n += 1

for key in mydict.keys():
    s = len(mydict[key])

    if s > 1:
        for i in range(s-1):
            for j in range(i+1, s):
                a = mydict[key][i]
                b = mydict[key][j]

                c = (2*a[0]-b[0], 2*a[1]-b[1])
                d = (2*b[0]-a[0], 2*b[1]-a[1])

                delta = (c[0] - a[0], c[1] - a[1])

                while (c[0] >= 0 and c[0] < n) and (c[1] >= 0 and c[1] < m): # and (c not in ant):
                    ant.add(c)
                    c = (c[0]+delta[0], c[1]+delta[1])

                delta = (d[0] - b[0], d[1] - b[1])
                while (d[0] >= 0 and d[0] < n) and (d[1] >= 0 and d[1] < m): # and (d not in ant):
                    ant.add(d)
                    d = (d[0] + delta[0], d[1] + delta[1])
                    

print(len(ant))

