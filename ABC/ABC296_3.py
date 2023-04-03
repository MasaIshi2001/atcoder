n,x = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))

a_lis2 = list(set(a_lis))

a_lis2.sort()

hidari = 0

migi = 1

if len(a_lis2) == 1 and x == 0:
    print("Yes")
    exit()
else:
    while migi < len(a_lis):
        if a_lis2[migi] - a_lis2[hidari] == x:
            print("Yes")
            exit()
        elif a_lis2[migi] - a_lis2[hidari] > x:
            hidari += 1
        elif a_lis2[migi] - a_lis2[hidari] < x:
            migi += 1

print("No")



