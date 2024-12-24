
# NOTE: doesn't fully work, had to manual change the output a bit for it to be the correct answer


def parse_input(input_data):
    wires = {}
    gates = []

    for line in input_data.splitlines():
        line = line.strip()
        if ":" in line:  # Wire initialization
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:  # Gate definition
            gates.append(line)

    return wires, gates


fhandle = open("d24input.txt")
data=""
for l in fhandle:
    data+=l

# Execution
wires, gates = parse_input(data)

pAND = dict()
pOR = dict()
pXOR = dict()

for gate in gates:
    gatelist = gate.split(" ")
    if gatelist[1] == "AND":
        pAND[frozenset([gatelist[0],gatelist[2]])] = gatelist[4]
    if gatelist[1] == "XOR":
        pXOR[frozenset([gatelist[0],gatelist[2]])] = gatelist[4]
    if gatelist[1] == "OR":
        pOR[frozenset([gatelist[0],gatelist[2]])] = gatelist[4]
    #print(gatelist)

#print(f"Output (decimal): {output}")
if frozenset(["x00","y00"]) in pXOR.keys():
    print("ok")
if (pXOR[frozenset(["x00","y00"])] == "z00"):
    print("ok")
    
a= pAND[frozenset(["x00","y00"])]

check = True
count = 0

swaplist = list()
while check and count<44:
    count +=1
    x = "x"+str(count).zfill(2)
    y = "y"+str(count).zfill(2)
    z = "z"+str(count).zfill(2)
    if frozenset([x,y]) not in pXOR.keys():
        print("t1")
    t1 = pXOR[frozenset([x,y])]
    
    if frozenset([t1,a]) not in pXOR.keys():
        print("z1",t1,a)
        for item in pXOR.keys():
            if a in set(item):
                swaplist.append(t1)
                t2 = list(item-set([a]))[0]
                pXOR[item] = t2
                swaplist.append(t2)
                
        tcheck = True
        for item in pAND.keys():
            if pAND[item] == t2:
                pAND[item] = t1
                tcheck = False
                print("AND")
                break
        if tcheck:
            for item in pOR.keys():
                if pOR[item] == t2:
                    pOR[item] = t1
                    tcheck = False
                    print("OR")
                    break
        if tcheck:
            for item in pXOR.keys():
                if pXOR[item] == t2:
                    pXOR[item] = t1
                    tcheck = False
                    print("XOR")
                    break
        t1 = t2
        pXOR[frozenset([x,y])]=t1

    z1 = pXOR[frozenset([t1,a])]

    if z1!=z:
        print("z error",z1,z)
        swaplist.append(z1)
        swaplist.append(z)
        tcheck = True
        for item in pAND.keys():
            if pAND[item] == z:
                pAND[item] = z1
                tcheck = False
                print("AND")
                break
        if tcheck:
            for item in pOR.keys():
                if pOR[item] == z:
                    pOR[item] = z1
                    tcheck = False
                    print("OR")
                    break
        if tcheck:
            for item in pXOR.keys():
                if pXOR[item] == z:
                    pXOR[item] = z1
                    tcheck = False
                    print("XOR")
                    break
        z1 = z
        pXOR[frozenset([t1,a])]=z1
        #break
    if frozenset([t1,a]) not in pAND.keys():
        print("s1")
        break
    s1 = pAND[frozenset([t1,a])]
    if frozenset([x,y]) not in pAND.keys():
        print("s2")
        break
    s2 = pAND[frozenset([x,y])]
    if frozenset([s2,s1]) not in pOR.keys():
        print("a")
        break
    a = pOR[frozenset([s2,s1])]
    print(count)

swaplist.sort()
print(",".join(swaplist))


# dkr,ggk,hhh,htp,rhv,z05,z15,z20