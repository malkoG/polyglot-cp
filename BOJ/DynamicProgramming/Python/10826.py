n=int(input())
a,b=0,1
for i in range(1,n):
    a,b=b,a+b
print(a if n == 0 else b)
            
