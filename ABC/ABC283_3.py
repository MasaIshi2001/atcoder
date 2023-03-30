s = str(input())
ans = 0
zCnt = 0
past = ""
for i in range(len(s)):
    if s[i] == "0":
        zCnt += 1
        ans += 1
    else:
        zCnt = 0
        ans += 1

    if zCnt == 2:
        zCnt = 0
        ans -= 1

print(ans)
