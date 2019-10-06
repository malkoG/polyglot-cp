
chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
mapping=dict()

for i, v in enumerate(chords):
    mapping[str(i)] = v
    mapping[v] = i

def process(s, d):
    result = 0
    try:
        result = mapping[s[:-1]] - 1 if s[-1] == 'b' else mapping[s]
    except:
        if s[-1] == '#':
            result = mapping[s[:-1]] + 1
    return mapping[str((result + d) % 12)]

while True:
    s = input()
    if s == "***":
        break
    d = int(input())
    print(" ".join([process(s, d) for s in s.split()]))
