fhandle = open("d13input.txt")
ans = 0
counter = 0

while True:
    line1 = fhandle.readline().strip()
    if line1 == "":
        break
    line2 = fhandle.readline().strip()
    line3 = fhandle.readline().strip()

    a = (line1.split()[2].split('+')[1].split(',')[0], line1.split()[3].split('+')[1])
    a = (int(a[0]), int(a[1]))
    b = (line2.split()[2].split('+')[1].split(',')[0], line2.split()[3].split('+')[1])
    b = (int(b[0]), int(b[1]))
    p = (line3.split()[1].split('=')[1].split(',')[0], line3.split()[2].split('=')[1])
    p = (int(p[0])+10000000000000, int(p[1])+10000000000000)

    fhandle.readline()
    

    b_tokens = ((p[0] * a[1]) - (p[1]*a[0]))/(b[0]*a[1] - b[1]*a[0])
    a_tokens = (p[0] - (b[0]*b_tokens))/a[0]

    # print(a, b, p)
    # print(a_tokens, b_tokens)

    if (a_tokens >= 0 and b_tokens >= 0 and a_tokens == int(a_tokens) and b_tokens == int(b_tokens)):
        ans_d = b_tokens + (a_tokens*3)
        ans += ans_d

print((ans))