symbols="abcdefghijklmnopqrstuvwxyz "
for i in range(int(input())):
    for word in input().split():
        val = 0
        for ch in word:
            val += symbols.find(ch)
        print(symbols[val % 27], end="")
    print("")
        
