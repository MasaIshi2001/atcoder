n = int(input())
c_lis = []
for i in range(n):
    s = str(input())
    c_lis.append(s)

kouho1 = ["H","D","C","S"]
kouho2 = ["1","2","3","4","5","6","7","8","9","10","j","q","k"]
for i in range(n):
    if c_lis[i][0] not in kouho1:
        print("No")
        exit()
    if c_lis[i][1] not in kouho2:
        print("No")
        exit()
    for j in range(n):
        if i != j:
            if c_lis[i] == c_lis[j]:
                print("No")
                exit()

print("Yes")