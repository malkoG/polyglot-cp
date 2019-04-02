words=dict()
words['.--'] = 'A'
words['-.'] = 'B'
words['---'] = 'C'
words['..'] = 'D'
words['--..'] = 'E'
words['--.-'] = 'F'
words['.-.'] = 'G'

patterns=['.--', '-.', '---', '..', '--..', '--.-', '.-.']

while True:
    result=''
    try:
        s=input()
    except:
        break
    invalid=False
    while s:
        if s[:2] in patterns:
            result+=words[s[:2]]
            s=s[2:]
        elif s[:3] in patterns:
            result+=words[s[:3]]
            s=s[3:]
        elif s[:4] in patterns:
            result+=words[s[:4]]
            s=s[4:]
        else:
            invalid=True
            break

    if invalid:
        print("could not be translated")
    else:
        print(result)
