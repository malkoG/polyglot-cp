def solve(alphabets, result, consonants, vowels, limit, depth):
    if depth > limit:
        return

    if depth == limit and len(result) == limit and consonants >= 2 and vowels >= 1:
        print(result)
        return

    for i in range(len(alphabets)):
        alphabet = alphabets[i]
        if alphabet in "aeiou":
            solve(alphabets[i+1:], result + alphabet, consonants, vowels + 1, limit, depth + 1)
        else:
            solve(alphabets[i+1:], result + alphabet, consonants + 1, vowels, limit, depth + 1)
        solve(alphabets[i+1:], result, consonants, vowels, limit, depth + 1)

limit, N = map(int, input().split())
alphabets = sorted(input().split())

solve(alphabets, "", 0, 0, limit, 0)
