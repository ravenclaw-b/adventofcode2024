fhandle = open("d10input.txt")

graph = {}
file = []
starts = []

for line in fhandle:
    line = line.strip()
    file.append(line)

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

def count_paths(start):
    stack = [(start, [start])]
    path_count = 0

    while stack:
        (current, path) = stack.pop()
        for neighbor in graph[current]:
            if neighbor not in path:
                if int(file[neighbor[0]][neighbor[1]]) == 9:
                    path_count += 1
                else:
                    stack.append((neighbor, path + [neighbor]))

    return path_count

total_paths = 0

for start in starts:
    total_paths += count_paths(start)

print(total_paths)