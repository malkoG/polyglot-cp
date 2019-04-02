import string

LEFT_PAREN, RIGHT_PAREN, HEX_DIGIT, ALPHABET, ENCLOSING, SPACE, COLON, AMP, HEX_START = range(9)

def translate(ch):
    if ch in string.hexdigits:
        return HEX_DIGIT
    elif ch in string.ascii_letters or ch in string.digits:
        return ALPHABET
    elif ch is '/':
        return ENCLOSING
    elif ch is '<':
        return LEFT_PAREN
    elif ch is '>':
        return RIGHT_PAREN
    elif ch is ' ':
        return SPACE
    elif ch is ';':
        return COLON
    elif ch is '&':
        return AMP
    elif ch is 'x':
        return HEX_START

while True:
    try:
        s=input()
        idx = 0
        stack = []
        
        invalid = False
        paren_open = False
        accepting_hexdigit = False
        self_closing = False
        closing = False

        tag_string = ""
        hex_string = ""
        
        while idx < len(s):
            ch = s[idx]
            symbol = translate(ch)
            
            if paren_open:
                if symbol in [LEFT_PAREN, SPACE]:
                    invalid = True
                    break
                elif symbol in [HEX_DIGIT, ALPHABET]:
                    if self_closing or ch in string.ascii_uppercase:
                        invalid = True
                        break
                    else:
                        tag_string += ch
                elif symbol is ENCLOSING:
                    if closing:
                        invalid = True
                        break
                    self_closing = not (not tag_string)
                    closing = True
                elif symbol is RIGHT_PAREN:
                    if closing:
                        if not self_closing:
                            if len(stack) == 0:
                                invalid = True
                                break
                            
                            if stack[-1] == tag_string:
                                stack.pop()
                            else:
                                invalid = True
                                break
                        closing = False
                        self_closing = False
                    else:
                        if not tag_string:
                            invalid = True
                            break
                        stack.append(tag_string)
                    paren_open = False
                    tag_string = ""
                else:
                    invalid = True
                    break
            elif accepting_hexdigit:
                if symbol is COLON:
                    accepting_hexdigit = False
                    if not len(hex_string) % 2 == 0:
                        invalid = True
                        break
                    hex_string = ""
                elif symbol is not HEX_DIGIT:
                    invalid = True
                    break
                elif symbol is HEX_DIGIT:
                    hex_string += ch
            else:
                if symbol is LEFT_PAREN:
                    paren_open = True
                elif symbol is RIGHT_PAREN:
                    invalid = True
                    break
                elif symbol is AMP:
                    testing_slice = s[idx:idx+5]
                    if '&lt;' in testing_slice:
                        idx += 3
                    elif '&gt;' in testing_slice:
                        idx += 3
                    elif '&amp;' in testing_slice:
                        idx += 4
                    elif '&x' in s[idx:idx+2]:
                        accepting_hexdigit = True
                        idx += 1
                    else:
                        invalid = True
                        break
                                    
            idx += 1

        if invalid or len(stack) > 0 or closing or paren_open or accepting_hexdigit:
            print("invalid")
        else:
            print("valid")
    except EOFError:
        break
