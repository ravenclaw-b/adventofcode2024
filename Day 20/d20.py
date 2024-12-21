import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.keys()}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

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

fromstart = dijkstra(adj, s)
fromend = dijkstra(adj, e)

norm = fromstart[e]
# print(norm)

ans = 0

for wall in walls:
    if (wall[0]-1, wall[1]) in adj.keys() and (wall[0]+1, wall[1]) in adj.keys():
        if fromstart[(wall[0]-1, wall[1])] + 2 + fromend[(wall[0]+1, wall[1])] <= norm-100:
            ans += 1
        if fromend[(wall[0]-1, wall[1])] + 2 + fromstart[(wall[0]+1, wall[1])] <= norm-100:
            ans += 1

    if (wall[0], wall[1]-1) in adj.keys() and (wall[0], wall[1]+1) in adj.keys():
        if fromstart[(wall[0], wall[1]-1)] + 2 + fromend[(wall[0], wall[1]+1)] <= norm-100:
            ans += 1
        if fromend[(wall[0], wall[1]-1)] + 2 + fromstart[(wall[0], wall[1]+1)] <= norm-100:
            ans += 1

print(ans)
        