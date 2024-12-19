fhandle = open("d11input.txt")
inp = fhandle.readline().strip()


_nums = inp.split()
for i in range(len(_nums)):
    _nums[i] = int(_nums[i])

nums = dict()
for num in _nums:
    nums[num] = 1

for j in range(75):
    temp = list(nums.keys())
    new = dict()
    for key in temp:
        if nums[key] != 0:
            l = len(str(key))
            if key == 0:
                if 1 in new.keys():
                    new[1] += nums[0]
                else:
                    new[1] = nums[0]
            elif l%2 == 0:
                p1 = int(str(key)[0:int(l/2)])
                p2 = int(str(key)[int(l/2):l])

                if p1 in new.keys():
                    new[p1] += nums[key]
                else:
                    new[p1] = nums[key]

                if p2 in new.keys():
                    new[p2] += nums[key]
                else:
                    new[p2] = nums[key]    
            else:
                p = key*2024
                if p in new.keys():
                    new[p] += nums[key]
                else:
                    new[p] = nums[key]
    nums = new

    # print(nums)

ans = 0
for key in nums.keys():
    ans += nums[key]

print(ans)

# 0 1 2 3