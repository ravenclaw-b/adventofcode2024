fhandle = open("d5input.txt")
counter = 0
ans = 0

S = set()
line = fhandle.readline().strip()

while len(line) != 0:
    S.add((int(line.split('|')[0]), int(line.split('|')[1])))
    counter += 1
    line = fhandle.readline().strip()

M = S.copy()
#for z in range(10, 100):
#    for x in range(10, 100):
#        for y in range(10, 100):
#            if ((x, z) in M) and ((z, y) in M):
#                M.add((x, y))


for line in fhandle:
    order = line.strip().split(',')
    l = len(order)
    for i in range(l):
        order[i] = int(order[i])
    check = True
    for i in range(l-1):
        for j in range(i+1, l):
            if (order[j], order[i]) in M:
               temp = order[i]
               order[i] = order[j]
               order[j] = temp
               check = False
    if not check:
        print(line)         
        ans += order[int((l-1)/2)]

print(ans)          