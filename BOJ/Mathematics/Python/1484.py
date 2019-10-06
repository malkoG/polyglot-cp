from math import ceil, floor

G=int(input())
result=[]
for a in range(1,100000):
    if G < a**2:
        break
    target=(G-a**2)/(a*2)
    ub=ceil(target)
    lb=floor(target)
    if ub == lb and target != 0:
        result.append(ub + a)

print(-1 if len(result) == 0 else "\n".join(map(str, list(sorted(set(result))))))
