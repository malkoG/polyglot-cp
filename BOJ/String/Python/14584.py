alphabet="abcdefghijklmnopqrstuvwxyz"
cipher=input()
words =[input() for i in range(int(input()))]
for i in range(26):
    translated = "".join([alphabet[(alphabet.find(ch) + i) % 26] for ch in cipher ])
    result = 0
    for word in words:
        result += translated.count(word)
    if result > 0:
        print(translated)
        break
