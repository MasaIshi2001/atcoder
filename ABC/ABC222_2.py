n,p = (int(x) for x in input().split())
a_list = list(map(int,input().split()))

huka = 0
for i in a_list:
    if i < p:
        huka = huka + 1

print(huka)
