pattern=input()
n=int(input())
answer=[]
for i in range(n):
    s=input()
    flag=True
    for i in range(len(s)):
        if pattern[i] == '*':
            continue

        if pattern[i] != s[i]:
            flag = False
    if flag:
        answer.append(s)

print(len(answer))
if len(answer) > 0:
    print("\n".join(answer))
