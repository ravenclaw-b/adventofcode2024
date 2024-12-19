def check (p, towel):
    dp = [0]*(len(towel)+1)
    dp[-1] = 1
    if towel[-1] in p:
        dp[-2] = 1
    for i in range(len(towel)-1, -1, -1):
        counter = 0
        for pattern in p:
            if towel[i:len(towel)].startswith(pattern):
                counter += dp[i+len(pattern)]
        dp[i] = counter
    return dp[0]

                
fhandle = open("d19input.txt")

patterns = fhandle.readline().strip().split(", ")
fhandle.readline()

t = []
for towel in fhandle:
    t.append(towel.strip())

ans = 0
counter = 0
for towel in t:
    ans += check(patterns, towel)

print(ans)