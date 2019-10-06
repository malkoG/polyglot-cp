while True:    
    n,m=map(int, input().split())
    if n==0 and m==0:
        break
    arr=list(map(int,input().split()))
    s=set(arr)
    counter={}
    for item in arr:
        try: counter[str(item)] += 1
        except: counter[str(item)] = 1
        
    answer=0
    for e in s:
        answer += 1 if counter[str(e)] > 1 else 0

    print(answer)
