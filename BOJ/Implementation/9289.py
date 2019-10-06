alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
morse=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
       '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
       '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'
]

mapping=dict()
for i,v in enumerate(morse):
    mapping[v] = alphabet[i]

for i in range(1, int(input())+1):
    print("Case {}: {}".format(i, "".join([ morse[word] for word in input().split() ])))
