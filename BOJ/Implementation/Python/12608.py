keys=[' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
keymap=dict()
for i in range(len(keys)):
    for ch in keys[i]:
        keymap[ch] = i

N=int(input())
for i in range(1,N+1):
    prev = 1
    s = input()
    ans = []
    for ch in s:
        current = keymap[ch]
        if prev == current:
            ans.append(' ')
        ans.append(str(current) * (keys[current].find(ch) + 1))
        prev = current

    print("Case #{}: {}".format( i, ''.join(ans)))
