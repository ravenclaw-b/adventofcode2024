fhandle = open("d23input.txt")
adj = dict()

for line in fhandle:
    line = line.strip()
    a = line.split("-")[0]
    b = line.split("-")[1]

    if a in adj.keys():
        adj[a].append(b)
    else:
        adj[a] = [b]

    if b in adj.keys():
        adj[b].append(a)
    else:
        adj[b] = [a]

trios = set()
for node in adj.keys():
    if node[0] == "t":
        for n1 in adj[node]:
            for n2 in adj[node]:
                if n1 != n2:
                    if n1 in adj[n2]:
                        trios.add(frozenset([n1, n2, node]))

print(len(trios))