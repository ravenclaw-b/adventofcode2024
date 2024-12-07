fhandle = open("d3input.txt")
strinput = fhandle.read()
state = 's'
ans = 0

begin = 0
end = 0

while(end != -1 and begin != -1):
    end = strinput.find("don't()", begin)

    if end == -1:
        finish = len(strinput)
    else:
        finish = end
        
    for i in range(begin, finish):
        place = strinput[i]
        match state:
            case 's':
                if place == 'm':
                    state = 'm'

            case 'm':
                if place == 'u':
                    state = 'u'
                else:
                    state = 's'

            case 'u':
                if place == 'l':
                    state = 'l'
                else:
                    state = 's'

            case 'l':
                if place == '(':
                    state = '('
                else:
                    state = 's'

            case '(':
                if place.isdigit():
                    x = int(place)
                    state = 'x'
                else:
                    state = 's'

            case 'x':
                if place.isdigit():
                    x = x*10 + int(place)
                    state = 'x'
                elif place == ',':
                    state = ','
                else:
                    state = 's'

            case ',':
                if place.isdigit():
                    y = int(place)
                    state = 'y'
                else:
                    state = 's'

            case 'y':
                if place.isdigit():
                    y = y*10 + int(place)
                    state = 'y'
                elif place == ')':
                    state = 's'
                    ans += x*y
                else:
                    state = 's'
    begin = strinput.find("do()", end)    

print(ans)
