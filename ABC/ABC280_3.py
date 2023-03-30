s = str(input())
t = str(input())

ans = 0

for i in range(len(s)):
    if s[i] != t[i]:
        ans = i+1
        break
    if i == len(s)-1:
        ans = i+1
        break

print(ans)

