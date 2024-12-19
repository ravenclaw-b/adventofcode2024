def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

fhandle = open("d18input.txt")

size = 71

adj = dict()
corrupted = []
for line in fhandle:
    line = line.strip()
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    corrupted.append((x, y))

c = set()
for i in range(1024):
    c.add(corrupted[i])

# print(c)

for i in range(size):
    for j in range(size):
        toadd = []
        if i < size-1 and (i+1, j) not in c: 
            toadd.append((i+1, j))

        if i > 0 and (i-1, j) not in c:
            toadd.append((i-1, j))

        if j > 0 and (i, j-1) not in c:
            toadd.append((i, j-1))

        if j < size-1 and (i, j+1) not in c:
            toadd.append((i, j+1))
        adj[(i, j)] = toadd

path = shortest_path(adj, (0, 0), (size-1, size-1))
# print(path)
print(len(path)-1)