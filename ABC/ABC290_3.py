
n,k = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))

a_lis.sort()
a_s = set(a_lis)

tmp = 0
for i in range(len(a_s)-1):
    if i+1 < k:
        if a_s[i+1] - a_s[i] == 1:
            tmp += 1
        else:
            print(tmp)
            exit()
    else:
        if a_s[i+1] - a_s[i] == 1:
            print(k)
            exit()
        else:
            print(k-1)
            exit()

