fhandle = open("d4input.txt")
matrix = []

for line in fhandle:
    matrix.append(line.strip())

word = "XMAS"
word_r = "SAMX"

word_index = 0
word_r_index = 0

ans = 0



for i in range(len(matrix)):
    word_index = 0
    word_r_index = 0
    for j in range(len(matrix[i])):
        if (matrix[i][j] == word[word_index]):
            word_index += 1
        elif (matrix[i][j] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[i][j] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[i][j] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
print(ans)


for j in range(len(matrix[0])):
    # print(j)
    word_index = 0
    word_r_index = 0
    for i in range(len(matrix)):
        if (matrix[i][j] == word[word_index]):
            word_index += 1
        elif (matrix[i][j] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[i][j] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[i][j] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
            #print(f"i: {i}, j: {j}")

        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
           # print(f"REVERSE i: {i}, j: {j}")

print(ans)

# diagonal
# -------------------------------------------------------------------------


for i in range(len(matrix[0])):
    k = 0
    word_index = 0
    word_r_index = 0
    while (i+k < len(matrix[0])):
        if (matrix[k][i+k] == word[word_index]):
            word_index += 1
        elif (matrix[k][i+k] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[k][i+k] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[k][i+k] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
           # print(f"k: {k}, k+i: {k+i}")
        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
            # print(f"REVERSE k: {k}, k+i: {k+i}")
        k += 1
print(ans)


for i in range(1, len(matrix)):
    k = 0
    word_index = 0
    word_r_index = 0
    while (i+k < len(matrix)):
        if (matrix[i+k][k] == word[word_index]):
            word_index += 1
        elif (matrix[i+k][k] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[i+k][k] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[i+k][k] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
        k += 1
print(ans)

# ---------------------------------------------------------------------


for i in range(len(matrix[0])):
    k = 0
    word_index = 0
    word_r_index = 0
    while (i-k >= 0):
        if (matrix[k][i-k] == word[word_index]):
            word_index += 1
        elif (matrix[k][i-k] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[k][i-k] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[k][i-k] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
        k += 1
print(ans)


for i in range(1,len(matrix)):
    k = 0
    word_index = 0
    word_r_index = 0
    while (i+k <len(matrix)):
        if (matrix[i+k][len(matrix[0])-k-1] == word[word_index]):
            word_index += 1
        elif (matrix[i+k][len(matrix[0])-k-1] == 'X'):
            word_index = 1
        else:
            word_index = 0

        if (matrix[i+k][len(matrix[0])-k-1] == word_r[word_r_index]):
            word_r_index += 1
        elif (matrix[i+k][len(matrix[0])-k-1] == 'S'):
            word_r_index = 1
        else:
            word_r_index = 0

        if (word_index == 4):
            ans += 1
            word_index = 0
        if (word_r_index == 4):
            ans +=  1
            word_r_index = 0
        k += 1
print(ans)