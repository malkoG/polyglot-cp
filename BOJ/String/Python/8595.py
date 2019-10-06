_=input()
digits='0123456789'
acc = 0
answer = 0
for ch in input():
    if ch in digits:
        acc *= 10
        acc += digits.find(ch)
    else:
        answer += acc
        acc = 0
answer += acc
print(answer)

