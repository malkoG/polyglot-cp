for i in range(1,int(input())+1):
    degree,*arr,_=map(int,input().split())
    c=0
    for j in range(degree,0,-1):
        arr[c] *= j
        c += 1
    print("Case {}: {} {}".format(i , degree-1, " ".join(map(str,arr))))
