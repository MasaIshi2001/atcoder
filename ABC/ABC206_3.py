n = int(input())
a_list = list(map(int,input().split()))
a_set = set(a_list)
sousuu = n*(n-1)/2

if len(a_set) == 1:
    print(0)
    exit()

a_list.sort()

tyouhuku = {}
pre_num = -1
pos = 0
for i in a_list:
    if i not in tyouhuku.keys():
        tyouhuku[i] = 0
    tyouhuku[i] = tyouhuku[i] + 1
    

herukazu = 0
for i in tyouhuku.values():
    if i > 1:
        herukazu += i*(i-1)/2

print(int(sousuu - herukazu))
