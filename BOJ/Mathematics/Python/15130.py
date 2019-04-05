seq = list(map(int,input().split()))
nz = []
for i in range(len(seq)):
    if seq[i] != 0:
        nz.append(i)

if (seq[nz[1]] - seq[nz[0]]) % (nz[1] - nz[0]):
    print(-1)
else:
    d = (seq[nz[1]] - seq[nz[0]]) // (nz[1]-nz[0])
    for i in range(len(seq)):
        print("{} ".format(seq[nz[0]] + (i-nz[0]) * d), end="")
