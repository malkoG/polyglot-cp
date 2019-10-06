def re_encode(s, k):
    if k == 0:
        return s

    ss = []
    for i in range(len(s)//2):
        ss.append(int(s[2*i]) * s[2*i+1])

    return re_encode("".join(ss), k-1)

k, pos = map(int, input().split())
print(re_encode(input(), k)[pos])
