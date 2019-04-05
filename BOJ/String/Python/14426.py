n,m=map(int,input().split())

prefix_dict = dict()
for i in range(n):
    s = input()
    for j in range(1,len(s)+1):
        prefix_dict[s[:j]] = True

ans = 0
for i in range(m):
    s = input()
    try: ans += 1 if prefix_dict[s] else 0
    except: pass

print(ans)
