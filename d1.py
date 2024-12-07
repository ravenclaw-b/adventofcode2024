infile = open("d1input.txt")

mapone = []
maptwo = []

for line in infile:
    mapone.append(int(line.split()[0]))
    maptwo.append(int(line.split()[1]))

mapone.sort()
maptwo.sort()

similarity = 0

for number in mapone:
    similarity += (maptwo.count(number)*number)

print(similarity)

# dif = 0

# for i in range(1000):
#     dif += abs(mapone[i]-maptwo[i])

# print(dif)

