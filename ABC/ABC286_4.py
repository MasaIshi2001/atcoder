n,x = (int(x) for x in input().split())
a_lis = []
b_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    a_lis.append(a)
    b_lis.append(b)
 
 
dp_lis = [[ 0 for i in range(x+1)] for j in range(n+1)]
dp_lis[0][0] = 1
 
for i in range(n):
    for k in range(x+1):
        for j in range(b_lis[i]+1):
            if k >= a_lis[i]*j:
                if dp_lis[i][k-a_lis[i]*j] == 1:
                    dp_lis[i+1][k] = 1
 
for i in dp_lis:
    if i[x] == 1:
      print("Yes")
      exit()
 
print("No")



