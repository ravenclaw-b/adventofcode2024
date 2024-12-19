fhandle = open("d14input.txt")
bots_p = []
bots_v = []
end_pos = []

tall = 103
wide = 101

for line in fhandle:
    line = line.strip()
    pos_x = int(line.split()[0].split("=")[1].split(",")[0])
    pos_y = int(line.split()[0].split("=")[1].split(",")[1])

    vel_x = int(line.split()[1].split("=")[1].split(",")[0])
    vel_y = int(line.split()[1].split("=")[1].split(",")[1])

    bots_p.append((pos_x, pos_y))
    bots_v.append((vel_x, vel_y))

for i in range(len(bots_p)):
    end_pos.append(((bots_p[i][0]+(bots_v[i][0]*100))%wide, (bots_p[i][1]+(bots_v[i][1]*100))%tall))
    print(end_pos[i])

lu = 0
ru = 0
ld = 0
rd = 0

for bot in end_pos:
    if bot[0] < (wide-1)/2 and bot[1] < (tall-1)/2:
        lu += 1
    elif bot[0] > (wide-1)/2 and bot[1] < (tall-1)/2:
        ru += 1
    elif bot[0] > (wide-1)/2 and bot[1] > (tall-1)/2:
        rd += 1
    elif bot[0] < (wide-1)/2 and bot[1] > (tall-1)/2:
        ld += 1



print(lu, rd, ld, ru)
print(lu*rd*ld*ru)
