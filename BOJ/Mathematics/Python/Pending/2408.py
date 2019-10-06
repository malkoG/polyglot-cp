from math import floor
answer=0
state =0
action="+"
for i in range(int(input())*2-1):
    if state == 0:
        number=int(input())
        if action=="+":
            answer += number
        elif action=="-":
            answer -= number
        elif action=="*":
            answer *= number
        else:
            answer = floor(answer / number)
        state = 1
    else:
        action=input()

print(answer)
