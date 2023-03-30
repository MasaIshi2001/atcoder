n = int(input())
a_lis = list(map(int,input().split()))

even_lis = []
kisuu_lis = []
for i in a_lis:
    if i%2 == 0:
        even_lis.append(i)
    else:
        kisuu_lis.append(i)

even_lis.sort(reverse=True)
kisuu_lis.sort(reverse=True)

max_e = -1
max_k = -1

if len(even_lis) > 1:
    max_e = even_lis[0] + even_lis[1]

if len(kisuu_lis) > 1:
    max_k = kisuu_lis[0] + kisuu_lis[1]

print(max(max_e,max_k))
        









