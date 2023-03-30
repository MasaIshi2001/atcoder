s = str(input())
ans = ""
for i in range(len(s)):
    if s[i] == "0":
        ans += "1"

    elif s[i] =="1":
        ans += "0"

print(ans)