target_string=input()
pattern=input()

result = ""
state_stack = []

pattern_length = len(pattern)
cursor = 0
for i in range(len(target_string)):
    result += target_string[i]
    if target_string[i] == pattern[cursor]:
        cursor += 1
    else:
        if target_string[i] == pattern[0]:
            state_stack.append(cursor)
            cursor = 1
        else:
            state_stack = []
            cursor = 0    

    if cursor == pattern_length:
        result = result[:-pattern_length]
        cursor = state_stack.pop() if len(state_stack) > 0 else 0
    
if result == "":
    print("FRULA")
else:
    print(result)
