n = int(input())
a_lis = list(map(int,input().split()))
m = int(input())
b_lis = list(map(int,input().split()))
x = int(input())

dp = [0 for i in range(x+1)]
available = [True for x in range(x+1)]
dp[0] = 1
for i in b_lis:
    available[i] = False

for i in range(x+1):
    if available[i] == False:
        dp[i] = 0
    else:
        for j in a_lis:
            if j <= i:
                dp[i] = dp[i-j] or dp[i]
                            

if dp[x] == 1:
    print("Yes")
else:
    print("No")