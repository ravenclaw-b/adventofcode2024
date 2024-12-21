def mymin(i, j, k):
    a = b = c = 9999999
    
    if (i, j) in distance.keys():
        a = distance[(i, j)]
    if (i, k) in distance.keys():
        b = distance[(i, k)]
    if (k, j) in distance.keys():
        c = distance[(k, j)]
    return min(a, b + c)

# Algorithm implementation
def floyd_warshall(G):
    counter = 0
    for k in G.keys():
        print(counter)
        counter += 1
        for i in G.keys():
            for j in G.keys():
                distance[(i, j)] = mymin(i, j, k)
    return

fhandle = open("d20input.txt")

inp = []
counter = 0
for line in fhandle:
    inp.append(list(line.strip()))

    temp = line.strip().find("S")
    if temp != -1:
        s = (counter, temp)

    temp = line.strip().find("E")
    if temp != -1:
        e = (counter, temp)
    counter += 1

adj = dict()

wide = len(inp[0])
tall = len(inp)

walls = []

for i in range(tall):
    for j in range(wide):
        if inp[i][j] == "#":
            walls.append((i, j))

for i in range(tall):
    for j in range(wide):
        toadd = []
        if (i, j) in walls:
            continue
        if i < tall-1 and inp[i+1][j] != "#": 
            toadd.append((i+1, j))

        if i > 0 and inp[i-1][j] != "#":
            toadd.append((i-1, j))

        if j > 0 and inp[i][j-1] != "#":
            toadd.append((i, j-1))

        if j < wide-1 and inp[i][j+1] != "#":
            toadd.append((i, j+1))
        adj[(i, j)] = toadd

distance = dict()
for key in adj.keys():
    for item in adj[key]:
        distance[(key, item)] = 1

floyd_warshall(adj)
norm = distance[(s, e)]

ans = 0

for wall in walls:
    if (wall[0]-1, wall[1]) in adj.keys() and (wall[0]+1, wall[1]) in adj.keys():
        if distance[(s, (wall[0]-1, wall[1]))] + 2 + distance[e, (wall[0]+1, wall[1])] <= norm-100:
            ans += 1
        if distance[(e, (wall[0]-1, wall[1]))] + 2 + distance[s, (wall[0]+1, wall[1])] <= norm-100:
            ans += 1

    if (wall[0], wall[1]-1) in adj.keys() and (wall[0], wall[1]+1) in adj.keys():
        if distance[(s, (wall[0], wall[1]-1))] + 2 + distance[e, (wall[0], wall[1]+1)] <= norm-100:
            ans += 1
        if distance[(e, (wall[0], wall[1]-1))] + 2 + distance[s, (wall[0], wall[1]+1)] <= norm-100:
            ans += 1

print(ans)
        