
n,w = (int(x) for x in input().split())
a_list = list(map(str,input().split()))

weight = [0 for i in range(w+1)]

for i in range(n):
    if w >= a_list[i]: 
        weight[a_list[i]] = 1

for i in range(n):
    for j in range(i+1,n):
        if w >= a_list[i]+a_list[j]:
            weight[a_list[i]+a_list[j]] = 1

for i in range(n):
    for j in range(i+1,n):
        for k in range(i+j+1,n):
            if w >= a_list[i]+a_list[j]+a_list[k]:
                weight[a_list[i]+a_list[j]+a_list[k]] = 1

print(weight.count(1))