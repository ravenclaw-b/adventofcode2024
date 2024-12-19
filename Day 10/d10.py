fhandle = open("d10input.txt")

graph = {}
file = []
starts = []

for line in fhandle:
    line = line.strip()
    file.append(line)

fhandle.close()  

for n in range(len(file)):
    for m in range(len(file[0])):
        toAdd = []
        if int(file[n][m]) == 0:
            starts.append((n, m))
        if m > 0 and int(file[n][m-1]) - int(file[n][m]) == 1:
            toAdd.append((n, m-1))
        if m < len(file[0]) - 1 and int(file[n][m+1]) - int(file[n][m]) == 1:
            toAdd.append((n, m+1))
        if n > 0 and int(file[n-1][m]) - int(file[n][m]) == 1:
            toAdd.append((n-1, m))
        if n < len(file) - 1 and int(file[n+1][m]) - int(file[n][m]) == 1:
            toAdd.append((n+1, m))
        graph[(n, m)] = toAdd

ans = 0

for start in starts:
    stack = graph[start]
    visited = [start]

    while stack:
        neigh = stack.pop()
        if neigh not in visited:
            visited.append(neigh)
            if int(file[neigh[0]][neigh[1]]) == 9:
                ans += 1
            else:
                stack.extend(graph[neigh])

print(ans)