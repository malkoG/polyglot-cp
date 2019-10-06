from math import ceil
while True:
    n=int(input())
    if n == 0:
        break
    arr=list(map(int, input().split()))
    avg=ceil(sum(arr)/n)
    print(len([i for i in arr if i <= avg]))
