
while True:
    acc = 0
    pc  = 0
    commands = []

    for i in range(32):
        try:
            s=input()
            commands.append(s)
        except:
            exit(0)

    while True:
        s = commands[pc]
        operator=s[0:3]
        operand=int(s[3:],2)
        
        pc += 1
        pc %= 32
        if operator=='000':
            commands[operand] = format(acc, '08b')
        elif operator=='001':
            acc = int(commands[operand],2)
        elif operator=='010':
            pc = operand if acc == 0  else pc
        elif operator=='011':
            pass
        elif operator=='100':
            acc += 255
            acc %= 256
        elif operator=='101':
            acc += 1
            acc %= 256
        elif operator=='110':
            pc = operand
        else:
            break

    print(format(acc, '08b'))

            
