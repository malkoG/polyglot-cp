n=int(input())
for i in range(n):
    pointer = 0
    byte_array = [0] * 32768
    
    left_stack  = [-1] * 128000
    right_stack = [-1] * 128000
    validation_stack = []
    command_length = 0
    command_array = []
    while True:
        try:
            line = input()
        except:
            break
        if line == "end":
            break
        for ch in line:
            if ch not in "<>+-.[]%":
                continue
            if ch == "%":
                break
            command_length += 1
            command_array.append(ch)
            
    command = "".join(command_array)
    left_brackets_count = command.count('[')
    left_stack = [-1] * left_brackets_count 
    right_stack = [-1] * left_brackets_count
    
    validation_stack = []
    frequency = 0
    scanning_index = 0

    positions_hashmap = {}
    valid = True
    for ch in command:
        if ch == "[":
            validation_stack.append((scanning_index, frequency,))
            frequency += 1
        elif ch == "]":
            if len(validation_stack) == 0:
                valid = False
                break
            left, stack_index = validation_stack.pop()
            right = scanning_index

            positions_hashmap[str(left)] = stack_index
            positions_hashmap[str(right)] = stack_index
            
            left_stack[stack_index] = right
            right_stack[stack_index] = left
            
        scanning_index += 1

    print("PROGRAM #{}:".format(i + 1))
    if not valid or len(validation_stack) > 0:
        print("COMPILE ERROR")
        continue

#    print(command)
    scanning_index = 0
    command_size = len(command)
    results_array = []
    while scanning_index < command_size:
        ch = command[scanning_index]
        if ch == ">":
            pointer += 1
            pointer %= 32768
        elif ch == "<":
            pointer += 32767
            pointer %= 32768
        elif ch == "+":
            byte_array[pointer] += 1
            byte_array[pointer] %= 256
        elif ch == "-":
            byte_array[pointer] += 255
            byte_array[pointer] %= 256
        elif ch == ".":
            print(chr(byte_array[pointer]), end='')
        elif ch == "[":
#            print("(pointer: {}, value: {}, scanning: {})".format(pointer, byte_array[pointer], scanning_index))
            stack_index = positions_hashmap[str(scanning_index)] 
            if byte_array[pointer] == 0:
                scanning_index=left_stack[stack_index]
        elif ch == "]":
#            print("(pointer: {}, value: {}, scanning: {})".format(pointer, byte_array[pointer], scanning_index))
            stack_index = positions_hashmap[str(scanning_index)]
            if byte_array[pointer] != 0:
                scanning_index=right_stack[stack_index]
        scanning_index += 1
                
    result = "".join(results_array)
    print("")
#    print(result)
