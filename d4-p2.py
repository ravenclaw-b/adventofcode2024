fhandle = open("d4input.txt")
matrix = []

for line in fhandle:
    matrix.append(line.strip())

n = len(matrix)
m = len(matrix[0])

ans = 0

for i in range(m-2):
    for j in range(n-2):
        if (matrix[i+1][j+1] == 'A'):
            if ((matrix[i][j] == 'S' and matrix[i+2][j+2] == 'M') or (matrix[i][j] == 'M' and matrix[i+2][j+2] == 'S')):
                if ((matrix[i+2][j] == 'S' and matrix[i][j+2] == 'M') or (matrix[i+2][j] == 'M' and matrix[i][j+2] == 'S')):
                    ans += 1

print(ans)