def solve(n):
    if n % 3 == 0:
        if n % 8 == 0:
            return '8' * (n//8)
        elif n % 5 == 0:
            return '5' * (n//5)
        
