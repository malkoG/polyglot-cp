alp="abcdefghijklmnopqrstuvwxyz"
while True:
    s=input()
    if s == "#":
        break
    a,b,c=s.split()
    advance=[]
    for i in range(len(a)):
        advance.append((26+alp.find(b[i])-alp.find(a[i])) % 26)
    d=""
    for i in range(len(a)):
        d += alp[(alp.find(c[i]) + advance[i]) % 26]
    print(a,b,c,d)
