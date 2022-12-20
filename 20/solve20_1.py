import os
f = open(f"{os.path.dirname(__file__)}/input20.txt", "r")
# f = open(f"{os.path.dirname(__file__)}/example20.txt", "r")

encrypted_file = []
original_pos = []
len_file = 0

for line in f.readlines():
    encrypted_file.append(int(line.strip()) )
    original_pos.append(len_file)
    len_file += 1

for p in range(len_file):
    # print(encrypted_file)
    i = original_pos.index(p)
    offset = encrypted_file[i]
    if( offset > 0 ):
        old_pos = i
        for j in range(offset):
            new_pos = ( old_pos + 1 ) % len_file
            tempV = encrypted_file[new_pos]
            encrypted_file[new_pos] = encrypted_file[old_pos]
            encrypted_file[old_pos] = tempV
            tempP = original_pos[new_pos]
            original_pos[new_pos] = original_pos[old_pos]
            original_pos[old_pos] = tempP
            old_pos = new_pos
    elif( offset < 0 ):
        old_pos = i
        for j in range(-offset):
            new_pos = ( old_pos - 1 + 2*len_file) % len_file
            tempV = encrypted_file[new_pos]
            encrypted_file[new_pos] = encrypted_file[old_pos]
            encrypted_file[old_pos] = tempV
            tempP = original_pos[new_pos]
            original_pos[new_pos] = original_pos[old_pos]
            original_pos[old_pos] = tempP
            old_pos = new_pos


pos_0 = encrypted_file.index(0)

print(encrypted_file)

print(encrypted_file[(pos_0+1000)%len_file], encrypted_file[(pos_0+2000)%len_file], encrypted_file[(pos_0+3000)%len_file], (encrypted_file[(pos_0+1000)%len_file]+encrypted_file[(pos_0+2000)%len_file]+encrypted_file[(pos_0+3000)%len_file]) )

# Nâo é 21743 (tá muito alto)
# Não é 12570 (tá muito alto)