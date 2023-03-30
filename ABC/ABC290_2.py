n,k = (int(x) for x in input().split())
s = str(input())

ans = ""
cnt = 0
for i in range(len(s)):
    if s[i] == "o":
        if cnt < k:
            ans += "o"
        else:
            ans+= "x"    
    else:
        ans+= "x"

print(ans)