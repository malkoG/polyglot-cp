digit='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def solve(s, fr, to):
    result=0
    for ch in s:
        result *= fr
        result += digit.find(ch)

    answer=""
    if result == 0:
        return "0"
    while result > 0:
        answer += digit[result % to]
        result = result // to
    return answer[::-1]

n=int(input())
for i in range(n):
    if i != 0:
        print()

    f,t,s=input().split()
    print(f, s)
    print(t, solve(s,int(f),int(t)))
