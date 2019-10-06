def solve(n):
    count  = 0
    answer = []
    while n > 0:
        if n % 2 == 1:
            answer.append(count)
        n //= 2
        count += 1
    return answer

while True:
    n=int(input())
    if n == 0:
        break
    print("{ " + (", ".join([ str(3**i) for i in solve(n-1) ]) + " }" if n != 1 else "}"))
