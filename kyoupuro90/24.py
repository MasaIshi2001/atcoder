n,k = (int(x) for x in input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

sa = 0
for i in range(n):
    sa += abs(a_list[i] - b_list[i])

if k % 2 != sa % 2 or sa > k:
    print("No")
else:
    print("Yes")