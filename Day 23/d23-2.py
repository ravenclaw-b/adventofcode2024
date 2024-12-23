fhandle = open("d23input.txt")
adj = dict()

for line in fhandle:
    line = line.strip()
    a, b = line.split("-")

    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]

    if b in adj:
        adj[b].append(a)
    else:
        adj[b] = [a]

fhandle.close()

largest = set()
best = 0

for node in adj.keys():
    clique = set([node])
    neighbors = set(adj[node])

    for neigh in neighbors:
        if all(neigh in adj[other] for other in clique):
            clique.add(neigh)

    if len(clique) > best:
        best = len(clique)
        largest = clique.copy()

largest = list(largest)
largest.sort()
password = ','.join(largest)

print(password)
print(largest)
print(best)

check = False
for a in largest:
    for b in largest:
        if a != b and a not in adj[b]:
            check = True

print(check)
