alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    s1=input()
    if s1 == "END":
        break
    s2=input()

    c1="".join(s1.split())
    c2="".join(s2.split())

    result1 = sum([ c1.count(alphabet) - 1 for alphabet in alphabets if c1.count(alphabet) > 1 ])
    result2 = sum([ c2.count(alphabet) - 1 for alphabet in alphabets if c2.count(alphabet) > 1 ])
    
    if result1 > result2:
        print(s2)
    else:
        print(s1)
