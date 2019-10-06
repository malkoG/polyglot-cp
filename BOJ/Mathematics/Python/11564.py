k,a,b=map(int,input().split())

aa=min(abs(a), abs(b))
bb=max(abs(a), abs(b))
if a*b > 0:
    print(bb//k-(aa-1)//k)
else:
    print(aa//k+bb//k+1)
