MIS=lambda: map(int, input().split())
a,b=MIS()
c,d=MIS()
result = 0
answer = 0
for i in range(4):
    tmp = a/c + b/d
    if result < tmp:
        result = tmp
        answer = i
    a,b,c,d=c,a,d,b
print(answer)
