
def clique (G, mask):
    if len(mask) == 0:
        return set()
    best = 0
    bestclique = set()
    for node in mask:
        mask = mask-set([node])
        tempclique = clique(G, mask & set(G[node]))
        if len(tempclique) >= best:
            best = len(tempclique)
            bestclique = tempclique | set([node])
    return bestclique


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

fhandle.close()

out = list(clique(adj, set(adj.keys())))
out.sort()
print(",".join(out))
