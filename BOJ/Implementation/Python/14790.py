digit="0123456789"

def check(s):
    flag = True
    for i in range(len(s)-1):
        flag = flag and digit.find(s[i]) >= digit.find(s[i-1])
    return flag

for i in range(1, int(input()) + 1):
    result=0
    for j in range(1, int(input() + 1)):
        if check("0" + str(j)):
            result = j

    print("Case #{}: {}".format(i, result))
