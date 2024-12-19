fhandle = open("d15input.txt")
matrix = []

linecount = 0
count = 0
line = " "

line = fhandle.readline().strip()
while line != "":
    matrix.append(list(line))

    count = 0
    for letter in line:
        if letter == "@":
            bot = [linecount, count]
        count += 1
    linecount += 1
    line = fhandle.readline().strip()

    
moves = ""
for line in fhandle:
    moves += line.strip()
moves = list(moves)

for move in moves:
    if move == "^":
        up = matrix[bot[0]-1][bot[1]]
        if up == ".":
            matrix[bot[0]-1][bot[1]] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[0] -= 1
        elif up == "O":
            temp = 1
            while matrix[bot[0]-temp][bot[1]] != "#" and matrix[bot[0]-temp][bot[1]] != ".":
                temp += 1
            if matrix[bot[0]-temp][bot[1]] == ".":
                matrix[bot[0]-temp][bot[1]] = "O"
                matrix[bot[0]-1][bot[1]] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[0] -= 1

    if move == "v":
        up = matrix[bot[0]+1][bot[1]]
        if up == ".":
            matrix[bot[0]+1][bot[1]] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[0] += 1
        elif up == "O":
            temp = 1
            while matrix[bot[0]+temp][bot[1]] != "#" and matrix[bot[0]+temp][bot[1]] != ".":
                temp += 1
            if matrix[bot[0]+temp][bot[1]] == ".":
                matrix[bot[0]+temp][bot[1]] = "O"
                matrix[bot[0]+1][bot[1]] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[0] += 1

    if move == ">":
        up = matrix[bot[0]][bot[1]+1]
        if up == ".":
            matrix[bot[0]][bot[1]+1] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[1] += 1
        elif up == "O":
            temp = 1
            while matrix[bot[0]][bot[1]+temp] != "#" and matrix[bot[0]][bot[1]+temp] != ".":
                temp += 1
            if matrix[bot[0]][bot[1]+temp] == ".":
                matrix[bot[0]][bot[1]+temp] = "O"
                matrix[bot[0]][bot[1]+1] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[1] += 1

    if move == "<":
        up = matrix[bot[0]][bot[1]-1]
        if up == ".":
            matrix[bot[0]][bot[1]-1] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[1] -= 1
        elif up == "O":
            temp = 1
            while matrix[bot[0]][bot[1]-temp] != "#" and matrix[bot[0]][bot[1]-temp] != ".":
                temp += 1
            if matrix[bot[0]][bot[1]-temp] == ".":
                matrix[bot[0]][bot[1]-temp] = "O"
                matrix[bot[0]][bot[1]-1] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[1] -= 1

print(len(matrix))
print(len(matrix[0]))
print(matrix)

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "O":
            ans += 100*i + j

print(ans)
