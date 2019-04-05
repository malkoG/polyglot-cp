n=int(input())
prefix,suffix=input().split('*')
for i in range(n):
    s=input()
    print("DA" if s[0:len(prefix)] == prefix and s[-len(suffix):] == suffix and len(s) == len(prefix) + len(suffix) else "NE")
