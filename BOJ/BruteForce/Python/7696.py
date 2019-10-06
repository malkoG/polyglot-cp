arr=[]
num = 1
counter = [0] * 10
while True:
    if len(arr) >= 1000000:
        break

    for i in range(10):
        counter[i] = 0
        
    target = num
    while target > 0:
        counter[target % 10] += 1
        target = target // 10

    flag = True
    for i in range(10):
        flag = flag and counter[i] <= 1
        
    if flag:
        arr.append(num)

    num += 1
        
while True:
    n=int(input())
    if n == 0:
        break
    print(arr[n-1])
