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


ans = 0
disksum=[]
disksum.append(0)
print(disk)


for i in range(1,l):
    disksum.append(disksum[i-1]+disk[i-1])



while forward<l:
    backward = l-1
    while (forward < backward):
        valb = disk[backward]
        idb = int(backward/2)
        valf = disk[forward]
        #print(disk)
        idx = disksum[forward]
        if (valb <= valf):
            for i in range(valb):
                ans = ans + idb*idx
                #print(idb, idx)
                idx+=1
            disk[forward] = valf-valb
            disk[backward] = 0
            disk[backward-1] = 0

        backward -= 2

    forward+=2
print(ans)
for i in range(l):
   
    if disk[i] > 0 and (i%2)==0:
       
        idx = disksum[i]
        idf = int(i/2)
        for i in range(idf):
            ans = ans + idf*idx
            #print(idb, idx)
            idx+=1

print(ans)
print(disksum)
print(disk)