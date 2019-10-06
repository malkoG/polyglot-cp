uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers=uppers.lower()
while True:
    s=input()
    if s=="#":
        break

    shift = uppers.find(s[-1])
    for ch in s[:-1]:
        if ch in uppers:
            idx = (uppers.find(ch) - shift + 26) % 26
            print(uppers[idx], end="")
        elif ch in lowers:
            idx = (lowers.find(ch) - shift + 26) % 26
            print(lowers[idx], end="")
        else:
            print(ch, end="")
    print("")
