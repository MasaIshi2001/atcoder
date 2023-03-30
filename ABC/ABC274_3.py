n = int(input())
a_list = list(map(int,input().split()))
cnt_lis = []
st = 1
pass_dic = {}
ans_lis = [0 for i in range(2*n+1)]
ans_lis[0]=0
ans_lis[1]=1
ans_lis[2]=1

for i in range(1,len(a_list)):
    ans_lis[i*2+1] = ans_lis[a_list[i]-1]+1
    ans_lis[i*2+2] = ans_lis[a_list[i]-1]+1
    
for i in ans_lis:
  print(i)










