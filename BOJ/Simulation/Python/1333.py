can_receive_call=[True] * (10**6+7)
N,L,D=map(int,input().split())
for i in range(0, 10**6+7, L+5):
    for j in range(0, L):
        can_receive_call[i+j]=False
for i in range(0, 10**6+7, D):
    if can_receive_call[i]:
        print(i)
        break
