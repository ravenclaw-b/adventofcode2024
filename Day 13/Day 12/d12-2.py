def check (x, y, letter):
    if (x < len(matrix) and x >= 0 and y < len(matrix[0]) and y >= 0):
        if matrix[x][y] == letter:
            matrix[x][y] = "."
            comps.add((x, y))
            check(x+1, y, letter)
            check(x-1, y, letter)
            check(x, y+1, letter)
            check(x, y-1, letter)

def calc (comps):
    l = len(comps)
    sides = []

    for comp in comps:
        sides.append((comp[0], comp[1], "u"))
        sides.append((comp[0], comp[1], "d"))
        sides.append((comp[0], comp[1], "r"))
        sides.append((comp[0], comp[1], "l"))

    sides_s = set(sides)

    for i in range(len(sides)-1):
        for j in range(i+1, len(sides)):
            # print(sides[i],sides[j])
            if sides[i][0] == sides[j][0] and sides[i][1]-sides[j][1] == 1:
                sides_s.discard((sides[j][0], sides[j][1], 'r'))
                sides_s.discard((sides[i][0], sides[i][1], 'l'))
            elif sides[i][0] == sides[j][0] and sides[i][1]-sides[j][1] == -1:
                sides_s.discard((sides[j][0], sides[j][1], 'l'))
                sides_s.discard((sides[i][0], sides[i][1], 'r'))
            elif sides[i][1] == sides[j][1] and sides[i][0]-sides[j][0] == 1:
                sides_s.discard((sides[j][0], sides[j][1], 'd'))
                sides_s.discard((sides[i][0], sides[i][1], 'u'))
            elif sides[i][1] == sides[j][1] and sides[i][0]-sides[j][0] == -1:
                sides_s.discard((sides[j][0], sides[j][1], 'u'))
                sides_s.discard((sides[i][0], sides[i][1], 'd'))
    # print(sides_s)
    p = len(sides_s)
    sides_s_l = list(sides_s)
    temp = p
    for i in range(p-1):
        for j in range(i+1, p):
            if sides_s_l[i][0] == sides_s_l[j][0] and abs(sides_s_l[i][1] - sides_s_l[j][1]) == 1 and ((sides_s_l[j][2] == "u" and sides_s_l[i][2] == 'u') or (sides_s_l[j][2] == "d" and sides_s_l[i][2] == 'd')):
                temp -= 1
            elif sides_s_l[i][1] == sides_s_l[j][1] and abs(sides_s_l[i][0] - sides_s_l[j][0]) == 1 and ((sides_s_l[j][2] == "r" and sides_s_l[i][2] == 'r') or (sides_s_l[j][2] == "l" and sides_s_l[i][2] == 'l')):
                temp -= 1

    return temp*l

fhandle = open("d12input.txt")
matrix = []
ans = 0

for line in fhandle:
    matrix.append(list(line.strip()))

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == ".": 
            continue
        comps = set()
        check(i, j, matrix[i][j])
        # print(comps)
        ans += calc(comps)

print(ans)