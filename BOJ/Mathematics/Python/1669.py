a,b=map(int, input().split())
d=b-a
acc = 0
for i in range(2**16):
    threshold = i
    acc = i*(i+1)
    if d <= i*(i+1):
        break

if d == 0:
    print(0)
else:
    print(2*threshold - 1 if d <= acc-threshold else 2*threshold)
