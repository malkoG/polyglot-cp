time=[ list(map(int, input().split(":"))) for i in range(2) ]
t=[ time[i][2] + 60 * ( time[i][0]*60 + time[i][1]) for i in range(2) ]
ans=(t[1]-t[0] + 86400) % 86400
print("{:02}:{:02}:{:02}".format((ans//60)//60, (ans//60)%60, ans%60))
