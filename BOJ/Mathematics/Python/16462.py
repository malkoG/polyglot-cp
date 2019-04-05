from math import ceil

def translate(s):
    t = list(s)
    if s != '100':
        for i in range(len(s)):
            if t[i] in '069':
                t[i] = '9'
    return "".join(t)

n=int(input())
scores=[ int(translate(input())) for i in range(n) ]
print(ceil(sum(scores)/len(scores)))
