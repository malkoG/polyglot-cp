d={}
d['M'] = 4
d['W'] = 3
d['C'] = 1
d['B'] = 2

name={}
name['M'] = "Mountain Lion"
name['W'] = "Wolf"
name['C'] = "Coyote"
name['B'] = "Bobcat"

for i in range(int(input())):
    s,p=input().split()
    counter = {}
    for ch in 'WMCB':
        counter[ch] = 0
    
    for ch in p:
        counter[ch] += d[ch]

    arr = []
    for ch in 'WMCB':
        arr.append((counter[ch], ch))

    arr.sort()
    print(s + ":", end=" ")
    if arr[-1][0] == arr[-2][0]:
        print("There is no dominant species")
    else:
        print("The " + name[arr[-1][1]] + " is the dominant species")
