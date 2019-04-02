T=int(input())
for i in range(1,T+1):
    print("Test set {}:".format(i))
    n=int(input())
    robots=[ input() for i in range(n)]

    phrases=int(input())
    inventory=dict()

    for i in range(phrases):
        names = input().split()
        for name in names:
            inventory[name] = True

    for robot in robots:
        try:
            flag = inventory[robot]
        except:
            flag = False

        print("{} is {}".format(robot, "present" if flag else "absent"))

    print()
