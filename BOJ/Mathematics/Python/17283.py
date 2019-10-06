L = int(input())
R = int(input())
answer = 0
acc = 1
while True:
    acc *= 2
    L *= R
    L //= 100
    if L < 5:
        break
    answer += L * acc
    
print(answer)
