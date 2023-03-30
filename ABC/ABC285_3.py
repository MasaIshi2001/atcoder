s = input()
ans = 0

for i in range(len(s)):
    tmp = ord(s[i]) - 64
    ans += tmp

print(ans)