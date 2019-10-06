from decimal import *

digits='0123456789'
while True:
    try: s=input()
    except: break
    fraction=s.split('.')[-1]
    result=Decimal(0.0)
    for i, ch in enumerate(fraction):
        result += Decimal(digits.find(ch))/(8**(i+1))
    
    print("{} [8] = {} [10]".format(s,result))
