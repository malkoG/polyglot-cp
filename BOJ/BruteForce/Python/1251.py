s=input()
arr=[]
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        arr.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])
        
print(sorted(arr)[0])
