s=input()
ss=s+" "
current=''
count=0
result=[]
for ch in ss:
    if ch == current:
        count += 1
    else:
        result.append(count)
        current = ch
        count = 1

print("Odd." if len([ i for i in result[1:] if i % 2 == 0 ]) == 0 else "Or not.")
