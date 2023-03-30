a,b =(int(x) for x in input().split())
lis = [[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15]]

if a-1 >= 8:
    print("No")
    exit()

if b in lis[a-1]:
    print("Yes")
else:
    print("No")