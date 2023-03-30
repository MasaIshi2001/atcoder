n,q = (int(x) for x in input().split())
a_list = list(map(int,input().split()))
Lrv_list = []
for i in range(q):
    l,r,v = (int(x) for x in input().split())
    Lrv_list.append([l,r,v])

kaisa = []
ans = 0
for i in range(len(a_list)-1):
    kaisa.append(a_list[i+1] - a_list[i])
    ans += abs(a_list[i+1] - a_list[i])


for i in Lrv_list:
    maeL = 0
    maeR = 0
    atoL = 0
    atoR = 0
    if i[0] != 1:
        maeL = abs(kaisa[i[0] - 2])
        kaisa[i[0] - 2] += i[2]
        atoL = abs(kaisa[i[0] - 2])
    if i[1] <= len(kaisa):
        maeR = abs(kaisa[i[1]-1])
        kaisa[i[1]-1] -= i[2]
        atoR = abs(kaisa[i[1]-1])
    
    ans += ((atoL+atoR) - (maeL+maeR))
    print(ans)
