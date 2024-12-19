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
    p = 4*l
    comps_list = list(comps)

    for i in range(l-1):
        for j in range(i+1, l):
            if comps_list[i][0] == comps_list[j][0] and abs(comps_list[i][1]-comps_list[j][1]) == 1:
                p -= 2
            elif comps_list[i][1] == comps_list[j][1] and abs(comps_list[i][0]-comps_list[j][0]) == 1:
                p -= 2
    return p*l

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
        ans += calc(comps)

print(ans)