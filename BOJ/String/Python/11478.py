s=input()
l=len(s)
d=dict()
for i in range(l):
        for j in range(i+1, l+1):
            slice = s[i:j]
            try: d[slice] += 1
            except: d[slice] = 1

print(len(d.items()))
