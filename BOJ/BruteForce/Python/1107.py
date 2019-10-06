target=int(input())
_=input()
broken_buttons=input().split()
pushes=10**9
for i in range(0, 1000000):
    teleport = str(i)
    digit_button_input = len(teleport)

    flag = True
    for broken_button in broken_buttons:
        flag = flag and (broken_button not in teleport)

    if flag:
        pushes = min(pushes, digit_button_input + abs(target-i))

print(min(pushes, abs(target-100)))
