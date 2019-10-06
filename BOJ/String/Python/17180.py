alphabets = " abcdefghijklmnopqrstuvwxyz"
_=input()

s=[input() for i in range(2) ]
arr=[[] for i in range(2) ]

for i in range(2):
    current = ' '
    count = 0
    for ch in s[i] + ' ':
        if current == ch:
            count += 1
        else:
            arr[i].append(current)
            count = 1
            current = ch

ss = [ ''.join(arr[i]) for i in range(2) ]
diff = abs(len(ss[0])-len(ss[1]))
sss = [None, None]
if len(ss[1]) > len(ss[1]):
    sss[0] = ss[0] + ' ' * diff
    sss[1] = ss[1]
else:
    sss[0] = ss[0]
    sss[1] = ss[1] + ' ' * diff

ans = 0
for i in range(len(sss[1])):
    ans += abs(alphabets.find(sss[0][i]) - alphabets.find(sss[1][i]))

print(ans)
