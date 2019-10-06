counting=[0] * 10
m,s=map(int, input().split())
mm,ss=map(int, input().split())
digits='0123456789'
for i in range(mm*60-m*60+ss-s+1):    
    minute  = str(i // 60)
    seconds = str(i % 60)
    
    for d in digits:
        if d in minute or d in seconds:
            counting[int(d)] += 1
print(counting[int(input())])
