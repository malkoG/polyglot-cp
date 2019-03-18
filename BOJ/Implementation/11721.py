text=input()
size=len(text)
for start in range(0,size//10+1):
    print(text[start*10:(start+1)*10])
