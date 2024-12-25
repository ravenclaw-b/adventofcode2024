fhandle = open("d25input.txt")

keys = list()
locks = list()

line = " "

while len(line)!=0:
    line = fhandle.readline()
    data = list()
    lockcheck = False
    if line.strip()=="#####":
        lockcheck = True
    while line.strip()!="":
        data.append(line.strip())
        line = fhandle.readline()


    numbers = list()
    for i in range(len(data[0])): 
        temp =0
        for j in range(len(data)):
            if data[j][i]=="#":
                temp+=1
        numbers.append(str(temp))

    if lockcheck:
        locks.append("".join(numbers))
    else:
        keys.append("".join(numbers))

ans = 0
for key in keys:
    for lock in locks:
        check = True
        for i in range(len(lock)):
            if (int(lock[i]) + int(key[i])) > 7:
                check = False
                break
        if check:
            ans += 1

print(ans)