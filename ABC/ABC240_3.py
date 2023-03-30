n,x = (int(x) for x in input().split())
ab_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_lis.append([a,b])

dp = [[0 for i in range(10001)] for j in range(n)]
dp[0][ab_lis[0][0]] = 1
dp[0][ab_lis[0][1]] = 1

for i in range(n):
    for j in range(10001):
        if j > a:
            if dp[i][j-ab_lis[i+1][0]] == 1:
                dp[i+1][j] == 1
            if dp[i][j-ab_lis[i+1][1]] == 1:
                dp[i+1][j] == 1
            
if dp[n-1][x] == 1:
    print("Yes")
else:
    print("No")