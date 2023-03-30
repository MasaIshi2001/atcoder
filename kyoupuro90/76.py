#円環は列iに戻して、列i同士を繋いだ列jを用いて擬似的円環を作る
#lower_bound = bisect_left
import bisect

n = int(input())
a_list = list(map(int,input().split()))
b_iist = []
sum = 0

for i in range(len(a_list)):
    sum += a_list[i]
    b_iist.append(sum)

sum = b_iist[n-1]
for i in range(len(a_list)):
    sum += a_list[i]
    b_iist.append(sum)

if b_iist[n-1] % 10 != 0:
    print("No")
    exit()

for i in range(n):
    goal = 