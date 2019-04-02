def t(c):
    if c == 'A': return 1
    else: return int(c)

while True:
    s=input()
    if s == '#':
        break

    cards=list(map(t, s.split()[:-1]))
    odd=len([c for c in cards if c % 2 == 1])
    even=len([c for c in cards if c % 2 == 0])

    if odd == even:
        print("Draw")
    else:
        print("Cheryl" if odd > even else "Tania")
