cipher = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
plain  = "V W X Y Z A B C D E F G H I J K L M N O P Q R S T U".split()

while True:
    s=input()
    if s=="ENDOFINPUT":
        break
    s=input()
    for ch in s:
        if ch in cipher:
            idx=cipher.find(ch)
            print(plain[idx], end="")
        else:
            print(ch, end="")
    s=input()
    print("")
