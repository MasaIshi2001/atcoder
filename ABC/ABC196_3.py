n = int(input())
ans = 0
tmp1 = 1
tmp = 11
while tmp <= n:
    tmp1 += 1
    tmp = int(str(tmp1)+str(tmp1))
    ans += 1
 
print(ans)