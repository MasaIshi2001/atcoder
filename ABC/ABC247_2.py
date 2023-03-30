ninnzuu = int(input())

seimei_list = []

for i in range(ninnzuu):
    seimei =list(map(str,input().split()))
    seimei_list.append(seimei)
    

sei_count = 0
mei_count = 0
flag = 0
idx = 0
idx2 = 0

for i in seimei_list:
    check_sei = i[0]
    check_mei = i[1]
    idx = idx + 1

    for j in seimei_list:
        idx2 =idx2 + 1
        if idx2 == idx:
            continue

        if check_sei == j[0]:
            sei_count += 1
        if check_sei == j[1]:
            sei_count += 1
        if check_mei == j[0]:
            mei_count += 1
        if check_mei == j[1]:
            mei_count += 1
        
    if sei_count >= 2 and mei_count >= 2:
        flag = 1
        break

    idx2 = 0
    sei_count = 0
    mei_count = 0

if flag == 1:
    print("No")
else:
    print("Yes")




