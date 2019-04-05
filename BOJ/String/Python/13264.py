s=input()
suffix_arr = [ (s[i:],i) for i in range(len(s))]
for p in sorted(suffix_arr):
    print(p[1])
