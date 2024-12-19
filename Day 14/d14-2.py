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

check = True
counter = 0
while (check):
    counter += 1
    for i in range(len(bots_p)):
        bots_p[i] = ((bots_p[i][0]+(bots_v[i][0]))%wide, (bots_p[i][1]+(bots_v[i][1]))%tall)
    if len(bots_p) == len(set(bots_p)):
        check = False
    
# Create a grid to display the pattern
grid = [["." for _ in range(wide)] for _ in range(tall)]
for x, y in bots_p:
    grid[y][x] = "#"

# Print the grid
for row in grid:
    print("".join(row))

# lu = 0
# ru = 0
# ld = 0
# rd = 0

# # for bot in end_pos:
# #     if bot[0] < (wide-1)/2 and bot[1] < (tall-1)/2:
# #         lu += 1
# #     elif bot[0] > (wide-1)/2 and bot[1] < (tall-1)/2:
# #         ru += 1
# #     elif bot[0] > (wide-1)/2 and bot[1] > (tall-1)/2:
# #         rd += 1
# #     elif bot[0] < (wide-1)/2 and bot[1] > (tall-1)/2:
# #         ld += 1

# print(lu, rd, ld, ru)
# print(lu*rd*ld*ru)
