while True:
    s=input()
    if s=='-1':
        break

    print("N={}:".format(s))
    if s==s[::-1]:
        print("No!!")
        continue

    counter = 0
    while True:
        if s=='6174' or s=='0':
            break
        ss=sorted(list(s))
        rs=reversed(ss)

        n1=int(''.join(ss))
        n2=int(''.join(rs))

        print("{}-{}={}".format(n2,n1,n2-n1))

        s = str(n2-n1)
        counter += 1
        
    print("Ok!! {} times".format(counter))
        
    
    
