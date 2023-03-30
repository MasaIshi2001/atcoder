n,q = map(int,input().split())
a_list = [((a,10**9) for a in map(int,input().split()))]
x_lis = []
for i in range(q):
    x = int(input())
    x_lis.append((x,i))

ax = sorted(a_list+x_lis)[::-1]

ans = [0]*q
cnt = 0
for x,i in ax:
    if i<q:
        ans[i] = cnt
    else:
        cnt = cnt + 1

print(*ans,sep="\n")
