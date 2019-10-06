alphabets="abcdefghijklmnopqrstuvwxyz"
for i in range(int(input())):
    n=int(input())
    words=input().split()
    idx=-1
    for i in len(words):
        if words[i][0] in alphabets:
            idx = i
            break
    if idx == -1:
        print(" ".join(words))
    else:
        print(" ".join([*words[idx+1:], words[idx], *words[:idx]]))
