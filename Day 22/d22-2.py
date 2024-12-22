fhandle = open("d22input.txt")
inp = []
for line in fhandle:
    inp.append(int(line.strip()))

def calc (x):
    new = (x*64) ^ x
    new = new % 16777216

    new = int(new/32) ^ new
    new = new % 16777216

    new = (new*2048) ^ new
    new = new % 16777216

    return new

prices = [[] for _ in range(len(inp))]
diff = [[0] * 2000 for _ in range(len(inp))]

for j in range(len(inp)):
    num = inp[j]
    for i in range(2000):
        prices[j].append(num%10)
        num = calc(num)

for i in range(len(diff)):
    for j in range(1, 2000):
        diff[i][j] = prices[i][j]-prices[i][j-1]

monkeys = [{} for _ in range(len(inp))]
for i in range(len(inp)):
    for j in range(1, 1996):
        current = (diff[i][j], diff[i][j+1], diff[i][j+2], diff[i][j+3])
        if current not in monkeys[i].keys():
            monkeys[i][current] = prices[i][j+3]

best = 0
for i in range(-9, 10):
    for j in range(-9, 10):
        for k in range(-9, 10):
            for l in range(-9, 10):
                temp = 0
                for m in range(len(monkeys)):
                    if (i, j, k, l) in monkeys[m].keys():
                        temp += monkeys[m][(i, j, k, l)]
                best = max(best, temp)
print(best)