digits = '01234567'
while True:
    try:
        s=input()
        for i in range(len(s)):
            if s[i] != '0' and s[i] != '.':
                pivot = i
                break

        result = 0
        acc = 125
        for ch in s[2:]:
            result *= 1000
            result += acc*digits.find(ch)
            acc *= 1000
            acc //= 8

        print(s, '[8]', '=', s[:pivot] + str(result), '[10]')
    except:
        break
    
