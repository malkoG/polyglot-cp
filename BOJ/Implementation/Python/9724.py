from bisect import bisect_left

arr=[]
for i in range(1, 1260):
    arr.append(i**3)
for i in range(1,int(input())+1):
    a,b=map(int,input().split())
    left=bisect_left(arr,a)
    right=bisect_left(arr,b)
         
    print("Case #{}: {}".format(i, right-left))
