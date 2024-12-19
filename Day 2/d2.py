fhandle = open("d2input.txt")

ans = 0
lines = 0

for line in fhandle:
    lines +=1
    nums = list()
    nums_str = line.split()
    for num in nums_str:
       nums.append(int(num))

    for j in range(-1, len(nums)):
        removed = list()
        isSafe = True

        for k in range(len(nums)):
            if (k != j):
                removed.append(nums[k])

        isIncreasing = False
        if (removed[0] < removed[1]):
            isIncreasing = True
        
        for i in range(len(removed)-1):
            if (isIncreasing and removed[i] >= removed[i+1]) or ((not isIncreasing) and removed[i] <= removed[i+1]):
                isSafe = False
                break
            if abs(removed[i] - removed[i+1]) > 3:
                isSafe = False
                break
        if isSafe:
            ans += 1
            break
print(ans)