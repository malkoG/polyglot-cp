x,y,W,S=map(int,input().split())
answer=0
if 2*W >= S:
    diagonal=min(x,y)
    answer+= S*diagonal
    x-=diagonal
    y-=diagonal
    
if W >= S:
    answer+= 2*S*(x//2)
    x-=(x//2)*2
    
    answer+= 2*S*(y//2)
    y-=(y//2)*2

answer += W*(x+y)
print(answer)
