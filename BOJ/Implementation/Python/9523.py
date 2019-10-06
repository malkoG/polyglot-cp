_=input()
result=[]
for token in input().split():
    if token in "+*":
        result.append(token)
        continue
    acc = 0
    for ch in token:
        if ch == "=":
            acc += 10
        elif ch == "-":
            acc += 5
        elif ch == ":":
            acc += 2
        else:
            acc += 1
    result.append(str(acc))
print(eval("".join(result)))
