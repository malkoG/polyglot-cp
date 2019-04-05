def translate(dotted_cash):
    over_dot, under_dot = map(int, dotted_cash.split("."))
    return over_dot * 100 + under_dot

while True:
    n=int(input())
    bank = dict()
    
    if n == 0:
        print("goodbye")
        break
    
    for i in range(n):
        account, cash = input().split()
        bank[account] = translate(cash)

    while True:
        command=input().split()
        if command[0] == "end":
            print("end")
            print("")
            input()
            break

        if command[0] == "create":
            _, account = command
            try:
                if bank[account] >= 0:
                    print("create: already exists")
            except KeyError:
                bank[account] = 0
                print("create: ok")
        elif command[0] == "deposit":
            _, account, cash = command
            try:
                bank[account] += translate(cash)
                print("deposit {}: ok".format(cash))
            except KeyError:
                print("deposit {}: no such account".format(cash))
        elif command[0] == "withdraw":
            _, account, cash = command
            try:
                translated_cash = translate(cash)
                if bank[account] < translated_cash:
                    print("withdraw {}: insufficient funds".format(cash))
                else:
                    bank[account] -= translated_cash
                    print("withdraw {}: ok".format(cash))
            except KeyError:
                print("withdraw {}: no such account".format(cash))
        else:
            _, source, target, cash = command
            translated_cash = translate(cash)
            try:
                _ = bank[source], bank[target]
                if source == target:
                    print("transfer {}: same account".format(cash))
                elif bank[source] < translated_cash:
                    print("transfer {}: insufficient funds".format(cash))
                else:
                    bank[source] -= translated_cash
                    bank[target] += translated_cash
                    if source[-1] != target[-1]:
                        print("transfer {}: interbank".format(cash))
                    else:
                        print("transfer {}: ok".format(cash))
            except KeyError:
                print("transfer {}: no such account".format(cash))
