from functools import reduce

def maximum_digit_product(n):
    if len(n) == 1:
        return int(n)

    original = int(n[0]) * maximum_digit_product(n[1:])
    downgraded = int(n[0])-1 if int(n[0]) > 1 else 1
    downgraded_product = downgraded * reduce(lambda x,y: x*y, map(int, ['9'] * (len(n) - 1))) 

    return max(original, downgraded_product)

n=input()
print(maximum_digit_product(n))
