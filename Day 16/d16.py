def find_path(facing, score, pos, bestscore,path):
    if score > bestscore[0]:
        return
    if matrix[pos[0]][pos[1]] == "E":
        bestscore[0] = score
        for p in path:
            optset.add(p)
        return
    state_key = (pos[0], pos[1], facing[0], facing[1])
    if state_key in state.keys():
        if state[state_key] < score:
            return
    
    state[state_key] = score
    
    # if len(state) % 500 ==0:
    #      print(state) 
    #      input()
    rows, cols = len(matrix), len(matrix[0])

    # Move Forward
    ahead = (pos[0] + facing[0], pos[1] + facing[1])
    if 0 <= ahead[0] < rows and 0 <= ahead[1] < cols and matrix[ahead[0]][ahead[1]] != "#":
        path.append(ahead)
        find_path(facing, score + 1, ahead, bestscore,path)
        path.pop()

    # Turn Left
    left_facing = (-facing[1], facing[0])
   
    find_path(left_facing, score + 1000, pos, bestscore,path)

    # Turn Right
    right_facing = (facing[1], -facing[0])
    find_path(right_facing, score + 1000, pos, bestscore,path)

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

bestscore = [102460]
state = dict()
optset = set()
path=[s]
find_path((0, 1), 0, s, bestscore, path)
print(bestscore)
print(len(optset))