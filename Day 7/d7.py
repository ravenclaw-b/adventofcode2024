def check(val, nums):
    if (len(nums) == 1 and nums[0] == val):
        return True
    elif ((nums[0] != val) and (len(nums) == 1) or nums[-1] > val):
        return False
    else:
        a = nums.pop()
        b = nums.pop()

        nums.append(a*b)
        c1 = check(val, nums.copy())
        nums.pop()
        
        nums.append(a+b)
        c2 = check(val, nums.copy())
        nums.pop()

        nums.append(int(str(a) + str(b)))
        c3 = check(val, nums.copy())

        if (c1 or c2 or c3):
            return True
        else:
            return False

ans = 0
fhandle = open("d7input.txt")

for line in fhandle:
    val = int(line.split(':')[0])
    nums = line.split(':')[1].split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    nums.reverse()

    if check(val, nums):
        ans += val

print(ans)