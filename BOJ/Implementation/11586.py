n=int(input())
mirror = [ input() for i in range(0,n) ]
state = int(input())
display = mirror[::-1] if state > 2 else mirror
for line in display:
    print(line if state % 2 == 1 else line[::-1])
