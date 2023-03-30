n = int(input())
s = str(input())

if n == 1:
    print(s)
    exit()

ans = ""
for i in range(len(s)-1):
    if s[i] == "n" and s[i+1] == "a":
        ans += "ny"
    else:
        ans += s[i]

print(ans)

