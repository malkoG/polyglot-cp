n,c=map(int, input().split())
arr=list(map(int, input().split()))
frequency=dict()
first_met=0
where=dict()
for e in arr:
    try:
        frequency[str(e)] += 1
    except:
        where[str(e)] = first_met
        frequency[str(e)] = 1

    first_met += 1

for p in sorted([ [ -frequency[str(e)], where[str(e)], e] for e in arr]):
    print(p[2], end=" ")
