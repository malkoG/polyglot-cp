from datetime import date
while True:
    d,m,y=map(int, input().split())
    print((date(y,m,d)-date(y,1,1)).days + 1)
