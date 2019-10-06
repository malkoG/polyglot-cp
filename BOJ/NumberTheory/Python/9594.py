while True:
    n=int(input())
    if n == -1:
        break
    power=-5
    ans = n+1
    while abs(power) <= n:
        ans += (n-abs(power)) if power > 0 else abs(power)-n 
        power *= -5

    print(ans)
