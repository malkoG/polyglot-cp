n,m=map(int,input().split())
arr = []
for i in range(n):
    number, price, value = map(int, input().split())
    arr.append((-value/price,price,number))

for ans in sorted(arr)[:m]:
    print(ans[2])
