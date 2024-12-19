import heapq

def find_lowest_score(matrix, start_pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
    rows, cols = len(matrix), len(matrix[0])
    heap = []
    visited = {}

    # Start facing East (index 1 in directions)
    heapq.heappush(heap, (0, start_pos, 1))

    while heap:
        score, (x, y), dir_index = heapq.heappop(heap)
        key = ((x, y), dir_index)
        if key in visited and visited[key] <= score:
            continue
        visited[key] = score

        if matrix[x][y] == 'E':
            return score

        # Move Forward
        dx, dy = directions[dir_index]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != '#':
            heapq.heappush(heap, (score + 1, (nx, ny), dir_index))

        # Turn Left
        left_dir = (dir_index - 1) % 4
        heapq.heappush(heap, (score + 1000, (x, y), left_dir))

        # Turn Right
        right_dir = (dir_index + 1) % 4
        heapq.heappush(heap, (score + 1000, (x, y), right_dir))

    return -1  # No path found

fhandle = open("d16input.txt")
matrix = [] 
counter = 0

for line in fhandle:
    line = line.strip()
    matrix.append(list(line))

    eloc = line.find("E")
    sloc = line.find("S")

    if eloc != -1:
        e = (counter, eloc)

    if sloc != -1:    
        s = (counter, line.find("S"))
        matrix[s[0]][s[1]] = "."

    counter += 1

lowest_score = find_lowest_score(matrix, s)
print(lowest_score)