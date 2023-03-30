#step1 入力
n = int(input())
cp_list = []
for i in range(n):
    seiseki = list(map(int,input().split()))
    cp_list.append(seiseki)

q = int(input())
query_list = []
for i in range(q):
    query = list(map(int,input().split()))
    query_list.append(query)

#step2 1組2組の累積和を取る

ans_line = ''
sum_one = [0]*(n+1)
sum_two = [0]*(n+1)
for i in range(1,n+1):
    
    sum_one[i] = sum_one[i-1]
    sum_two[i] = sum_two[i-1]
    if cp_list[i-1][0] == 1:
        sum_one[i] += cp_list[i-1][1]
    elif cp_list[i-1][0] == 2:
        sum_two[i] += cp_list[i-1][1]
    

#step3 queryに答える
for i in query_list:
    ans1 = sum_one[i[1]] - sum_one[i[0]-1]
    ans2 = sum_two[i[1]] - sum_two[i[0]-1]
    print(str(ans1) + " " + str(ans2))



    
