n = int(input())
a_lis = list(map(int,input().split()))
b_lis = list(map(int,input().split()))
c_lis = list(map(int,input().split()))

cnt = [0 for i in range(n)]

for i in range(n):
    cnt[b_lis[c_lis[i]]] += 1

ans = 0
for i in range(n):
    ans += cnt[a_lis[i]]

print(ans)
