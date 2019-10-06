prev=0
count=0
digit="0123456789"
acc=0
for ch in input():
    if prev == 1:
        if ch == "0":
            acc   += 10
            count += 1
        else:
            acc   += prev
            count += 1
            if ch == "1":
                pass
            else:
                acc += digit.find(ch)
                count += 1
    else:
        if ch == "1":
            pass
        else:
            acc += digit.find(ch)
            count += 1

    prev = digit.find(ch)

if prev == 1:
    acc += prev
    count += 1

print("%.2f" % (acc/count))
