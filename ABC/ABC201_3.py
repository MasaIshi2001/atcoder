s = str(input())

ans = 0

for i in range(10000):
    tmp = i
    flag1 = True
    flag = [0 for i in range(10)]
    for j in range(4):
        tmp2 = tmp%10
        flag[tmp2] = 1
        tmp = tmp//10
    
    for k in range(10):
        if s[k] == "o" and flag[k] == 0:
            flag1 = False
        if s[k] == "x" and flag[k] == 1:
            flag1 = False

    if flag1 == True:
        ans += 1

print(ans)



    