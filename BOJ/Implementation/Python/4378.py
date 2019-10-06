m=dict()
A="1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,."
B="234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./"
for i in range(len(A)):
    m[B[i]]=A[i]
    
while True:
    try:
        s=input()
    except:
        break

    for ch in s:
        if ch in B:
            print(m[ch], end='')
        else:
            print(ch,end='')

    print()
