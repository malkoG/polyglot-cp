n=int(input())
for i in range(n):
    s= [ int(ch) for ch in input() ]
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] *= 2
            if(s[i] >= 10):
                s[i] = s[i] // 10 + s[i] % 10

    print("T" if sum(s) % 10 == 0 else "F")
