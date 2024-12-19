fhandle = open("d6input.txt")
lab = []
n = 0

mydict = {}

for line in fhandle:
    
    sline = line.strip()
    lab.append(list("o" + sline + "o"))
    temp = sline.find('^')
    if temp != -1:
        y = temp
        x = n
    n += 1

y += 1
x += 1
start_x = x
start_y = y
m = len(lab[0])-2
state = "up"

lab.insert(0, list("o"*(m+2)))
lab.append(list("o"*(m+2)))
lab_new = lab.copy()

while (lab[x][y] != "o"):
    #print(x)

    match state:
        case "up":
            if (lab[x-1][y] == '#'):
                state = "right"
            else:
                lab[x][y] = 'x'
                x -= 1

        case "right":
            if (lab[x][y+1] == '#'):
                state = "down"
            else:
                lab[x][y] = 'x'
                y += 1

        case "down":
            if (lab[x+1][y] == '#'):
                state = "left"
            else:
                lab[x][y] = 'x'
                x += 1

        case "left":
            if (lab[x][y-1] == '#'):
                state = "up"
            else:
                lab[x][y] = 'x'
                y -= 1
   

ans = 0

for line in lab:
    for letter in line:
        if letter == "x":
            ans += 1

print(ans)
counter = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if lab[i][j] == 'x' and (i!=start_x or j!= start_y):
            x = start_x
            y = start_y
            lab_new[i][j] = '#'
            check_loop = False
            cc = 0
            state = "up"

            while (lab_new[x][y] != "o"):
                match state:
                    case "up":
                        if (lab_new[x-1][y] == '#'):
                            state = "right"
                        else:
                            x -= 1

                    case "right":
                        if (lab_new[x][y+1] == '#'):
                            state = "down"
                        else:
                            y += 1

                    case "down":
                        if (lab_new[x+1][y] == '#'):
                            state = "left"
                        else:
                            x += 1

                    case "left":
                        if (lab_new[x][y-1] == '#'):
                            state = "up"
                        else:
                            y -= 1
                cc+=1
                if cc > 4*(n+2)*(m+2):
                    check_loop = True
                    break
            if check_loop:
                counter+=1
                #print((i,j))
                #print(counter)
            lab_new[i][j] = '.'
            
print(counter)

                    

