plain= "abcdefghijklmnopqrstuvwxyz"
cipher="ynficwlbkuomxsevzpdrjgthaq"

for i in range(1, int(input()) + 1):
    result=""
    for ch in input():
        if ch in cipher:
            result += plain[cipher.find(ch)]
        else:
            result += ch
    print("Case #{}: {}".format(i, result))
