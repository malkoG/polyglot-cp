c,s=input().split()
d=dict()
if c == 'E':
    ss = s + ' '
    current = ''
    count = ''
    result = []
    for ch in ss:
        if current == ch:
            count += 1
        else:
            result.append((current, count))
            count = 1
            current = ch
    print(''.join([ ch + str(cnt) for ch, cnt in result ]))
else:
    for i in range(len(s)//2):
        print(s[2*i] * int(s[2*i+1]), end='')
