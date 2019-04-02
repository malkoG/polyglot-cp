n=int(input())
for i in range(n):
    words = input().split()
    new_words = []

    for word in words:
        idx = -1
        for i in range(len(word)):
            if word[i] in 'aeiou':
                idx = i
                break
        if len(word) == 1:
            new_words.append(word + 'yay' if word in 'aeiou' else 'ay')
        elif idx == -1:
            new_words.append(word + 'ay')
        else:
            new_words.append(word[idx:] + word[:idx] + ('yay' if word[0] in 'aeiou' else 'ay'))

    print(" ".join(new_words))
