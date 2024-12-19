def check(p, towel, memo=None):
    if memo is None:
        memo = {}
    if towel in memo:
        return memo[towel]
    if len(towel) == 0:
        return True
    for pattern in p:
        if towel.startswith(pattern):
            if check(p, towel[len(pattern):], memo):
                memo[towel] = True
                return True
    memo[towel] = False
    return False

fhandle = open("d19input.txt")

patterns = fhandle.readline().strip().split(", ")
fhandle.readline()

t = []
for towel in fhandle:
    t.append(towel.strip())

ans = 0
counter = 0
for towel in t:
    if check(patterns, towel):
        ans += 1
        # print(towel)
    counter += 1
    # print(counter)

print(ans)