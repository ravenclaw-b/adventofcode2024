from copy import copy, deepcopy
def checkup (x, boxes):
    new = set()
    for b in boxes:
        if matrix[x-1][b] == "#":
            return False
        
        if matrix[x-1][b] == "]":
            new.add(b)
            new.add(b-1)
        elif matrix[x-1][b] == "[":
            new.add(b)
            new.add(b+1)
    if len(new) == 0:
        return True
    else:
        return checkup(x-1, new)
    
def checkdown (x, boxes):
    new = set()
    for b in boxes:
        if matrix[x+1][b] == "#":
            return False
        
        if matrix[x+1][b] == "]":
            new.add(b)
            new.add(b-1)
        elif matrix[x+1][b] == "[":
            new.add(b)
            new.add(b+1)
    if len(new) == 0:
        return True
    else:
        return checkdown(x+1, new)
    
def moveup (x, boxes):
    new = set()
    for b in boxes:
        if matrix[x-1][b] == "]":
            new.add(b)
            new.add(b-1)
        elif matrix[x-1][b] == "[":
            new.add(b)
            new.add(b+1)

    for b in new:
        if b in boxes:
            newmatrix[x-1][b] = matrix[x][b]
        else:
            newmatrix[x-1][b] = "."
    

    for b in boxes:
         newmatrix[x-1][b] = matrix[x][b]
  
    if len(new) != 0:
        moveup(x-1, new)
    else:
        
        for b in boxes:
            newmatrix[x-1][b] = matrix[x][b]  

def movedown (x, boxes):
    new = set()
    for b in boxes:
        if matrix[x+1][b] == "]":
            new.add(b)
            new.add(b-1)
        elif matrix[x+1][b] == "[":
            new.add(b)
            new.add(b+1)
    for b in new:
        if b in boxes:
            newmatrix[x+1][b] = matrix[x][b]
        else:
            newmatrix[x+1][b] = "."
    
    for b in boxes:
         newmatrix[x+1][b] = matrix[x][b]

    if len(new) != 0:
        movedown(x+1, new)
    else:
        for b in boxes:
            newmatrix[x+1][b] = matrix[x][b]  

fhandle = open("d15input.txt")
matrix = []

linecount = 0
count = 0
line = " "

line = fhandle.readline().strip()
while line != "":
    temp = []
    count = 0

    for letter in line:
        if letter == "@":
            temp += ["@", "."]
        elif letter == "O":
            temp += ["[", "]"]
        elif letter == "#":
            temp += ["#", "#"]
        elif letter == ".":
            temp += [".", "."]

        count += 1
    linecount += 1

    matrix.append(temp)
    line = fhandle.readline().strip()


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=="@":
            bot = [i,j]


moves = ""
for line in fhandle:
    moves += line.strip()
moves = list(moves)


# for line in matrix:
#     for letter in line:
#         print(letter, end="")
#     print() 
print(len(moves))
cc = 0
for move in moves:
    #print()
    #for line in matrix:
    #     for letter in line:
    #         print(letter, end="")
    #     print()
    #input()
    if move == "^":
        up = matrix[bot[0]-1][bot[1]]
        if up == ".":
            matrix[bot[0]-1][bot[1]] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[0] -= 1
        elif up == "[" or up == "]":
            boxes = set()
            if up == "[":
                boxes.add(bot[1])
                boxes.add(bot[1]+1)
                if checkup(bot[0]-1, boxes):
                    newmatrix = deepcopy(matrix)
                    moveup(bot[0]-1, boxes)
                    matrix = newmatrix.copy()

                    matrix[bot[0]][bot[1]] = "."
                    matrix[bot[0]-1][bot[1]] = "@"
                    matrix[bot[0]-1][bot[1]+1] = "."
                    bot[0] -= 1
            else:
                boxes.add(bot[1])
                boxes.add(bot[1]-1)
                if checkup(bot[0]-1, boxes):
                    newmatrix = deepcopy(matrix)
                    moveup(bot[0]-1, boxes)
                    matrix = newmatrix.copy()
                    matrix[bot[0]][bot[1]] = "."
                    matrix[bot[0]-1][bot[1]] = "@"
                    matrix[bot[0]-1][bot[1]-1] = "."
                    bot[0] -= 1
                
    if move == "v":
        up = matrix[bot[0]+1][bot[1]]
        if up == ".":
            matrix[bot[0]+1][bot[1]] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[0] += 1
        elif up == "[" or up == "]":
            boxes = set()
            if up == "[":
                boxes.add(bot[1])
                boxes.add(bot[1]+1)
                if checkdown(bot[0]+1, boxes):
                    
                    newmatrix = deepcopy(matrix)
                    movedown(bot[0]+1, boxes)
                    matrix = newmatrix.copy()
                    matrix[bot[0]][bot[1]] = "."
                    matrix[bot[0]+1][bot[1]] = "@"
                    matrix[bot[0]+1][bot[1]+1] = "."
                    bot[0] += 1
            else:
                boxes.add(bot[1])
                boxes.add(bot[1]-1)
                if checkdown(bot[0]+1, boxes):
                    newmatrix = deepcopy(matrix)
                    movedown(bot[0]+1, boxes)
                    matrix = newmatrix.copy()

                    matrix[bot[0]][bot[1]] = "."
                    matrix[bot[0]+1][bot[1]] = "@"
                    matrix[bot[0]+1][bot[1]-1] = "."
                    bot[0] += 1

    if move == ">":
        up = matrix[bot[0]][bot[1]+1]
        if up == ".":
            matrix[bot[0]][bot[1]+1] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[1] += 1
        elif up == "[":
            temp = 1
            while matrix[bot[0]][bot[1]+temp] != "#" and matrix[bot[0]][bot[1]+temp] != ".":
                temp += 1
            if matrix[bot[0]][bot[1]+temp] == ".":
                for i in range(2, temp+1):
                    if i%2 == 0:
                        matrix[bot[0]][bot[1]+i] = "["
                    else:
                        matrix[bot[0]][bot[1]+i] = "]"

                matrix[bot[0]][bot[1]+1] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[1] += 1

    if move == "<":
        up = matrix[bot[0]][bot[1]-1]
        if up == ".":
            matrix[bot[0]][bot[1]-1] = "@"
            matrix[bot[0]][bot[1]] = "."
            bot[1] -= 1
        elif up == "]":
            temp = 1
            while matrix[bot[0]][bot[1]-temp] != "#" and matrix[bot[0]][bot[1]-temp] != ".":
                temp += 1
            if matrix[bot[0]][bot[1]-temp] == ".":
                for i in range(2, temp+1):
                    if i%2 == 0:
                        matrix[bot[0]][bot[1]-i] = "]"
                    else:
                        matrix[bot[0]][bot[1]-i] = "["

                matrix[bot[0]][bot[1]-1] = "@"
                matrix[bot[0]][bot[1]] = "."
                bot[1] -= 1

    #print(move)

# print(len(matrix))
# print(len(matrix[0]))
# print(matrix)

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "[":
            ans += 100*i + j

print(ans)
print()
for line in matrix:
    for letter in line:
        print(letter, end="")
    print()
