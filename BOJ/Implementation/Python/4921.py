fits=dict()
fits['1']='45'
fits['2']=''
fits['3']='45'
fits['4']='23'
fits['5']='8'
fits['6']='23'
fits['7']='8'
fits['8']='67'

n=1
while True:
    s=input()
    if s=='0':
        break
    flag = s[0]=='1' and s[-1]=='2'

    for i in range(len(s)-1):
        flag = flag and s[i+1] in fits[s[i]]

    print(str(n)+".", "VALID" if flag else "NOT")
