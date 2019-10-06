alphabet="abcdefghijklmnopqrstuvwxyz"
while True:
    d,m,y=map(int, input().split())
    if d==0 and m==0 and y==0:
        break
    shift=(d+m+y) % 25 + 1
    for ch in input():
        if ch in alphabet:
            print(alphabet[(26+alphabet.find(ch)-shift) % 26], end="")
        else:
            print(ch,end="")

    print()
