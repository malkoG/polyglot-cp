import string

def f(n):
    if n==0:
        return
    else:
        f((n-1)//26)
        print(string.ascii_uppercase[(n+25)%26] ,end="")
    
while True:
    s=input()
    
    for i in range(len(s)):
        if s[i] == 'R':
            ridx = i
        elif s[i] == 'C':
            cidx = i

    if(s[cidx+1] == '0'):
        break
            
    f(int(s[cidx+1:]))
    print(int(s[1:cidx]))
