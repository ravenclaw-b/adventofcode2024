def operand (n):
    if n <= 3:
        return n
    elif n == 4:
        return A[0]
    elif n == 5:
        return B[0]
    elif n == 6:
        return C[0]
    else:
        return -1

def opcode (n, oper):
    x = operand(oper)
    if n == 0:
        A[0] = int(A[0]/pow(2, x))
    elif n == 1:
        B[0] = B[0]^oper
    elif n == 2:
        B[0] = x%8
    elif n == 3:
        if A[0] != 0:
            point[0] = oper
            point[0] -= 2
    elif n == 4:
        B[0] = B[0]^C[0]
    elif n == 5:
        ans.append(x%8)
        l = len(ans)
        if l > len(p) or ans[l-1] != p[l-1]:
            return -1
    elif n == 6:
        B[0] = int(A[0]/pow(2, x))
    else:
        C[0] = int(A[0]/pow(2, x))
    
    point[0] += 2
    return 0

p = [2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0]
count = 140000000
ans = []
while ",".join([str(s) for s in ans]) != ",".join([str(s) for s in p]):
    ans = []
    A = [count]
    B = [0]
    C = [0]
    point = [0]

    if count%1000000 == 0 :
        print(count)

    while point[0] < len(p):
        if opcode(p[point[0]], p[point[0]+1]) == -1:
            count += 1 
            break
    count += 1 