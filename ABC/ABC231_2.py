n = int(input())
namae_lis = []
for i in range(n):
    namae = str(input())
    namae_lis.append(namae)


if len(namae_lis) == 1:
    print(namae_lis[0])
    exit()
    
namae_lis.sort()
dic = {}
cnt = 1
for i in range(len(namae_lis)):
    if 1 <= i and i < len(namae_lis) - 1 :
        if past == namae_lis[i]:
            cnt = cnt + 1
        else:
            dic[past] = cnt
            cnt = 1
    elif i == len(namae_lis) - 1:
        if past == namae_lis[i]:
            cnt = cnt + 1
            dic[past] = cnt
        else:
            dic[past] = cnt
            dic[namae_lis[i]] = 1

    past = namae_lis[i]
    
print(max(dic.items(), key = lambda x:x[1])[0])