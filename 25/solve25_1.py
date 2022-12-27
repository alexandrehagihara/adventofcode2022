import os
f = open(f"{os.path.dirname(__file__)}/input25.txt", "r")

def snafu2dec(snafu):
    dec = 0
    for c in snafu:
        if( c == '1'):
            dec = dec*5 + 1
        elif( c == '2' ):
            dec = dec*5 + 2
        elif( c == '0' ):
            dec = dec*5
        elif( c == '-'):
            dec = dec*5 - 1
        elif( c == '='):
            dec = dec*5 - 2

    return dec

def dec2snafu(dec):
    snafu = ""
    while( dec > 0 ):
        digit = dec % 5 
        dec = dec // 5
        if( digit < 3 ): # 0,1,2
            snafu = str(digit) + snafu
        elif digit == 3: # 3 vira (5-2)
            snafu = '=' + snafu
            dec += 1 # carry
        elif digit == 4: # 4 vira (5-1)
            snafu = '-' + snafu
            dec += 1 # carry
    return snafu

total = 0
for l in f.readlines():
    total += snafu2dec(l.strip())

print(total)
print(dec2snafu(total))