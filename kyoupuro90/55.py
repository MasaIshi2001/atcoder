n,p,q = (int(x) for x in input().split())

a_list = list(map(int,input().split()))

cnt = 0

for i in range(len(a_list)-4):
    for j in range(i+1,len(a_list)-3):
        for k in range(j+1,len(a_list)-2):
            for l in range(k+1,len(a_list)-1):
                for m in range(l+1,len(a_list)):
                    if (((((((a_list[i]*a_list[j])%p)*a_list[k])%p*a_list[l])%p)*a_list[m])%p) == q:
                        cnt = cnt + 1

print(cnt)
