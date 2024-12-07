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
m = len(lab[0])-2
state = "up"

lab.insert(0, list("o"*(m+2)))
lab.append(list("o"*(m+2)))


while (lab[x][y] != "o"):
    #print(x)

    match state:
        case "up":
            if (lab[x-1][y] == '#'):
                state = "right"
            else:
                lab[x][y] = 'x'
                
                if (x, y) in mydict.keys():
                    mydict[(x, y)] = mydict(x, y).append('u') 
                else:
                    mydict[(x, y)] = ['u']

                x -= 1

        case "right":
            if (lab[x][y+1] == '#'):
                state = "down"
            else:
                lab[x][y] = 'x'

                if (x, y) in mydict.keys():
                    mydict[(x, y)] = mydict(x, y).append('r') 
                else:
                    mydict[(x, y)] = ['r']

                y += 1

        case "down":
            if (lab[x+1][y] == '#'):
                state = "left"
            else:
                lab[x][y] = 'x'

                if (x, y) in mydict.keys():
                    mydict[(x, y)] = mydict(x, y).union('d') 
                else:
                    mydict[(x, y)] = ['d']

                x += 1

        case "left":
            if (lab[x][y-1] == '#'):
                state = "up"
            else:
                lab[x][y] = 'x'

                if (x, y) in mydict.keys():
                    mydict[(x, y)] = mydict(x, y).union('x') 
                else:
                    mydict[(x, y)] = ['x']

                y -= 1
   

# ans = 0

# for line in lab:
#     for letter in line:
#         if letter == "x":
#             ans += 1

# print(ans)