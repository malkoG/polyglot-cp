c=1
while True:
    o,w=map(int, input().split())
    if o == 0 and w == 0:
        break

    flag = True:
    while True:
        command,amount=input().split()
        if command == '#':
            break
        if command == "F":
            w += int(amount)
        else:
            w -= int(amount)
        if w <= 0:
            flag = False
    
    print(c, end=" ")
    if flag:    
        if w > o//2 and w < 2*o:
            print(":-)")
        else:
            print(":-(")
    else:
        print("RIP")
    c+=1
