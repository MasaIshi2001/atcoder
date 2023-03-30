n = int(input())
a_list = []
for i in range(n):
    a_line = list(map(int,input().split()))
    a_list.append(a_line)

flag = 0
for i in range(n):
    for j in range(i):
        if i == j: #taikaku
            if a_list != "-":
                flag = 1
                break
        else: #taikaku igai
            if a_list[i][j] == "W": #kattete
                if a_list[j][i] != "L": #maketenakattra
                    flag = 1
                    break
            elif a_list[i][j] == "L": #makete
                if a_list[j][i] != "W": #kattenakattra
                    flag = 1
                    break
            elif a_list[i][j] == "D": #makete
                if a_list[j][i] != "D": #kattenakattra
                    flag = 1
                    break
            else:
                flag = 1
                break

if flag == 1:
    print("incorrect")
else:
    print("correct")
            