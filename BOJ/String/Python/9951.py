c=0
while True:
    s=input()
    if s=='#':
        break

    if c > 0:
        print("")
    words=s.split()
    excludes="'-\"?!,."
    digits="0123456789"
    
    result=set()
    for word in words:
        base = ""
        for ch in word.lower():
            if ch not in excludes:
                base += ch

        if(len([ ch for ch in word if digits.count(ch) > 0] ) == len(word)):
            continue
        
        if len(base) != 0:
            result.add(base)

    print("\n".join(sorted(result)))
    c += 1
