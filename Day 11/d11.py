fhandle = open("d11input.txt")
inp = fhandle.readline().strip()

nums = inp.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

for j in range(75):
    newnums = []
    for i in range(len(nums)):        
        l = len(str(nums[i]))
        if nums[i] == 0:
            newnums.append(1)
        elif l%2 == 0:
            newnums.append(int(str(nums[i])[0:int(l/2)]))
            newnums.append(int(str(nums[i])[int(l/2):l]))
        else:
            newnums.append(nums[i]*2024)
    nums = newnums

print(len(nums))

# 0 1 2 3