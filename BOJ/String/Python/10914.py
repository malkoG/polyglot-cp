alphabet="abcdefghijklmnopqrstuvwxyz"
n=int(input())
result=[]
for word in input().split():
    s=""
    for i in range(len(word)//2):
        s+=alphabet[(alphabet.find(word[2*i]) + alphabet.find(word[2*i+1]) - n + 26) % 26]
    result.append(s)
    
print(" ".join(result))
