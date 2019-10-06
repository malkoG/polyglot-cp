from math import log, floor

N=int(input())-1
counter = 1
result = 0.0
arr = []
while True:
    result += log(counter, 10)
    floored_value = int(floor(result))
    if int(floor(result)) > N:
        break

    if floored_value == N:
        arr.append(counter)
    
    counter += 1

if len(arr) == 0:
    print("NO")
else:
    print(len(arr))
    print("\n".join(map(str, arr)))
