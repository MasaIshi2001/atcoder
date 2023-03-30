N = int(input())
A = list(map(int,input().split()))
num = [0]*(N+1) #配列の初期化
for a in A:
    num[a-1] += 1

sm = 0

for i in range(N):
    sm += num[i]*(num[i]-1)/2


for i in range(N):
    ans = sm
    ans -= (num[A[i]-1]*(num[A[i]-1] - 1))/2
    ans += ((num[A[i]-1] - 1)*(num[A[i]-1] - 2))/2
    print(int(ans))