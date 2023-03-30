n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))

a_dic = {}
b_dic = {}
c_dic = {}

for i in range(46):
    a_dic[i] = 0
    b_dic[i] = 0
    c_dic[i] = 0

for i in a_list:
    a_dic[i%46] = a_dic[i%46] + 1

for i in b_list:
    b_dic[i%46] = b_dic[i%46] + 1

for i in c_list:
    c_dic[i%46] = c_dic[i%46] + 1

cnt = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k)%46 == 0:
                cnt = cnt + a_dic[i]*b_dic[j]*c_dic[k]

print(cnt)