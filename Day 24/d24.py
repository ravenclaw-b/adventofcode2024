import re

def parse_input(input_data):
    wires = {}
    gates = []

    for line in input_data.splitlines():
        line = line.strip()
        if ":" in line: 
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line: 
            gates.append(line)

    return wires, gates

def evaluate_gate(gate, wires):
    match = re.match(r"(.+?) (AND|OR|XOR) (.+?) -> (.+)", gate)
    if match:
        input1, operation, input2, output = match.groups()
        if input1.isdigit():
            val1 = int(input1)
        else:
            val1 = wires.get(input1, None)

        if input2.isdigit():
            val2 = int(input2)
        else:
            val2 = wires.get(input2, None)

        if val1 is not None and val2 is not None:
            if operation == "AND":
                wires[output] = val1 & val2
            elif operation == "OR":
                wires[output] = val1 | val2
            elif operation == "XOR":
                wires[output] = val1 ^ val2

    return wires

def simulate_gates(wires, gates):
    pending_gates = gates[:]

    while pending_gates:
        next_pending = []
        for gate in pending_gates:
            prev_state = wires.copy()
            evaluate_gate(gate, wires)

            if wires == prev_state:  
                next_pending.append(gate)

        if len(next_pending) == len(pending_gates):
            break  

        pending_gates = next_pending

    return wires

def calculate_output(wires):
    z_outputs = {key: value for key, value in wires.items() if key.startswith("z")}
    print(z_outputs)
    binary_number = "".join(str(z_outputs[f"z{i:02}"]) for i in range(len(z_outputs)))
    
    print(binary_number)
    binary_number = binary_number[::-1]
    print(binary_number)
    return int(binary_number, 2)


fhandle = open("d24input.txt")
data=""
for l in fhandle:
    data+=l

wires, gates = parse_input(data)
#print(wires)
#print(gates)
wires = simulate_gates(wires, gates)
output = calculate_output(wires)
print(f"Output: {output}")
