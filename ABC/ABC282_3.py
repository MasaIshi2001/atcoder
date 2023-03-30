n = int(input())
s = str(input())

kuku = False
ans = ""
for i in range(len(s)):
    if s[i] == '"':
        if kuku == False:
            kuku = True
            ans += '"' 

        else:
            kuku = False
            ans += '"'
    elif s[i] == ',':
        if kuku == False:
            ans += "."
        else:
            ans += ","
    else:
        ans += s[i]

print(ans)

