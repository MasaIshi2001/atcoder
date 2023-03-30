s= str(input())
dicS = {}
s_list = list(s)

for i in s_list:
    if i not in dicS:
        dicS[i] += 1
    else:
        dicS[i] = 1

for i in dicS.values():
    if i%2 == 1:
        print("No")
        exit()
    
print("Yes")

