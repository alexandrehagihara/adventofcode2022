import os
f = open(f"{os.path.dirname(__file__)}/input20.txt", "r")
# f = open(f"{os.path.dirname(__file__)}/example20.txt", "r")

encrypted_file = []
flag_pass = []

for line in f.readlines():
    encrypted_file.append(int(line.strip()) )
    flag_pass.append(False)

while(False in flag_pass):
    # print(encrypted_file)
    for i in range(len(flag_pass)):
        if not flag_pass[i]:
            offset = encrypted_file[i]
            new_pos = offset + i
            if( new_pos > len(encrypted_file) ):
                new_pos = (new_pos + 1) % len(encrypted_file)
            elif( new_pos < 1 ):
                new_pos = (new_pos - 1 + len(encrypted_file)) % len(encrypted_file)
            
            encrypted_file = encrypted_file[:i] + encrypted_file[i+1:]
            encrypted_file = encrypted_file[:new_pos] + [offset] + encrypted_file[new_pos:]
            flag_pass = flag_pass[:i] + flag_pass[i+1:]
            flag_pass = flag_pass[:new_pos] + [True] + flag_pass[new_pos:]
            break

pos_0 = encrypted_file.index(0)

print(encrypted_file)

print(encrypted_file[(pos_0+1000)%len(encrypted_file)], encrypted_file[(pos_0+2000)%len(encrypted_file)], encrypted_file[(pos_0+3000)%len(encrypted_file)], (encrypted_file[(pos_0+1000)%len(encrypted_file)]+encrypted_file[(pos_0+2000)%len(encrypted_file)]+encrypted_file[(pos_0+3000)%len(encrypted_file)]) )

# Nâo é 21743 (tá muito alto)
# Não é 12570 (tá muito alto)