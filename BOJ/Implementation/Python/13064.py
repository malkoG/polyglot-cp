cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="0123456789"
for i in range(int(input())):
    s=input()
    if s[0] in digit and s[0] == s[1] and s[2] in digit and s[3] in digit and s[4] in cap and s[5] in digit and s[6] in digit and s[7] in digit:
        print(s)
