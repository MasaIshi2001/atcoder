n = int(input())
list_n = []
for i in range(2*n+1):
    list_n.append(i+1)
while True:
    if len(list_n) != 0:
        print(list_n[0])
        del list_n[0]
        x = int(input())
        if len(list_n) != 0:
            list_n.remove(x)
    else:
         break
    