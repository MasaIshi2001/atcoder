n = int(input())
a_list = list(map(int,input().split()))
a_dic = {}
for i in range(n):
    a_dic[i+1] = a_list[i]

dic2 = sorted(a_dic.items(),key=lambda x:x[1])
print(dic2[len(dic2)-2][0]) 