s = str(input())

ans = []
for i in range(len(s)):
    if s[i] == "6":
        ans.append("9")
    elif s[i] == "9":
        ans.append("6")
    else:
        ans.append(s[i])

ans.reverse()
print("".join(ans))
