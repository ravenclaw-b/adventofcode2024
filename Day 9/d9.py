fhandle = open("d9input.txt")
line = fhandle.readline().strip()

isSpace = False

disk = []
counter = 0

for digit in line:
    disk.append(int(digit))

l = len(disk)
forward = 0
backward = l-1
valf = disk[forward]
idx = 0
idf = int(forward/2)

ans = 0


for i in range(valf):
    ans = ans + idf*idx
    #print(idf, idx)
    idx+=1
disk[forward] = 0
forward+=1
valf = disk[forward]

if backward%2 != 0:
    backward -= 1

while (forward < backward):
    valb = disk[backward]
    idb = int(backward/2)
    valf = disk[forward]
    #print(disk)
    if (valb <= valf):
        for i in range(valb):
            ans = ans + idb*idx
            #print(idb, idx)
            idx+=1
        disk[forward] = valf-valb
        disk[backward] = 0
        disk[backward-1] = 0
        backward -= 2
        
    else:
        for i in range(valf):
            ans = ans + idb*idx
            #print(idb, idx)
            idx+=1

        disk[backward] = valb - valf
        disk[forward] = 0
        forward += 1

        if (forward > backward): break
        valf = disk[forward]
        idf = int(forward/2)

        for i in range(valf):
            ans = ans + idf*idx
            #print(idf, idx)
            idx+=1
        disk[forward] = 0
        forward+=1

print(ans)
print(idx)