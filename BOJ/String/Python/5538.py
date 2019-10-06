def joi(i):
    return "J" * i + "O" * i + "I" * i
answer = 0
s=input()
jcount=0
i = 0
while i < len(s):
    if s[i] == "J":
        jcount += 1
        i += 1
    elif s[i] == "O":
        idx = i-jcount
        if jcount > 0 and s[idx:idx+3*jcount] == joi(jcount):
            answer += 1
            i = idx + 3*jcount
        else:
            i += 1
        jcount = 0
    else:
        i += 1
        jcount = 0
    print(i, jcount, answer)

print(answer)
