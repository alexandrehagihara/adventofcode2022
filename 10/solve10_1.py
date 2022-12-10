import os
# f = open(f"{os.path.dirname(__file__)}/example10.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input10.txt", "r")

# Valores iniciais
x,cycles = 1,0

check_cycles = [20, 60, 100, 140, 180, 220]

acc_signal = 0

for l in f.readlines():
    operation = l.split()
    if operation[0] == "noop":
        cycles += 1
        if cycles in check_cycles:
            print( operation,cycles, x, cycles*x)
            acc_signal += cycles * x
    elif operation[0] == "addx":
        cycles += 1
        if cycles in check_cycles:
            print(operation, cycles, x, cycles*x, "mid")
            acc_signal += cycles * x
        cycles += 1
        if cycles in check_cycles:
            print(operation, cycles, x, cycles*x, "end")
            acc_signal += cycles * x
        x += int(operation[1])
    

print(acc_signal)