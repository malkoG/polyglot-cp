while True:
    counter = [0] * 10
    try:
        n=int(input())
    except:
        break

    for k in range(1, 20):
        term = n * k
        for digit in str(term):
            counter[int(digit)] += 1
            
        result = len([ counter[i] for i in range(10) if counter[i] > 0])
        if result == 10:
            print(k)
            break
        
