digit="0123456789ACDEFHJKLMNPRTVWX"
coef=[2,4,5,7,8,10,11,13]

for t in range(int(input())):
    n,s=input().split()
    result=0
    answer=0
    for i in range(8):
        answer *= 27
        result += digit.find(s[i]) * coef[i]
        answer += digit.find(s[i])
    print(n, answer if digit[result % 27] == s[-1] else "Invalid")
