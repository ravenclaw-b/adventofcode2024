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

ans = 0
for i in range(len(inp)):
    num = inp[i]
    for j in range(2000):
        num = calc(num)
    ans += num
print(ans)