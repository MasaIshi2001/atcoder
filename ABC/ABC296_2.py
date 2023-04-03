ban = []
retu = ["a","b","c","d","e","f","g","h"]
for i in range(8):
    s = str(input())
    ban.append(s)
 
ans = ""
for i in range(len(ban)):
    for j in range(8):
        if ban[i][j] == "*":
            ans += retu[j]
            ans += str(8-i)
            print(ans)
            exit()
