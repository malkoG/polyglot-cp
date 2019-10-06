mirror=dict()
mirror['b'] = 'd'
mirror['d'] = 'b'
mirror['q'] = 'p'
mirror['p'] = 'q'

for ch in 'iovwx':
    mirror[ch] = ch

while True:
    s=input()
    if s =="#":
        break
    result = ''
    flag = True
    for ch in s:
        try:
            s += mirror[ch]
        except:
            flag = False
            break

    if flag:
        print(result)
    else:
        print("INVALID")

    
