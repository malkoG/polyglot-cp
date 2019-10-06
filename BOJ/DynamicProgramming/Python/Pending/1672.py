d=dict()
d['A'] = 'ACAG'
d['G'] = 'CGTA'
d['C'] = 'ATCG'
d['T'] = 'GAGT'
n=input()
s=input()
current = s[-1]
for ch in s[:-1][::-1]:
    idx = d[current].find(ch)
    current = d[current][idx]
print(current)
