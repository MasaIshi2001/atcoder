s = str(input())
s_dic = {}
lParePos = []
pos = 0
sStack = []
mojiCnt = 0

for i in range(len(s)):
    if s[i] == "(":
        lParePos.append(mojiCnt)
        pos += 1
        lParePos.append(0)
    elif s[i] == ")":
        num = lParePos.pop()
        pos -= 1
        for i in range(num):
            s_dic[sStack.pop()] = False

    else:
        if s[i] in s_dic.keys():
            if s_dic[s[i]] == True:
                print("No")
                exit()
        s_dic[s[i]] = True
        sStack.append(s[i])
        lParePos[pos] += 1

print("Yes")

