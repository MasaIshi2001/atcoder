import bisect
 
n,m = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))
b_lis = list(map(int,input().split()))
 
a_lis.sort()
kouho = []
 
for i in range(m):
    a = bisect.bisect_left(a_lis,b_lis[i])
    #b = bisect.bisect_right(a_lis,b_lis[i])
    if a == 0:
      min_num = abs(a_lis[0]-b_lis[i])
    elif a == len(a_lis):
      min_num = abs(a_lis[-1]-b_lis[i])
    else:
      min_num = min(abs(a_lis[a-1]-b_lis[i]),abs(a_lis[a]-b_lis[i]))
    kouho.append(min_num)
 
print(min(kouho))

