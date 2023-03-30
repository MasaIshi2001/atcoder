n,x = (int(x) for x in input().split())
a_list = list(map(int,input().split()))

for i in range(len(a_list)):
    if (i+1) % 2 == 0:
        a_list[i] = a_list[i] - 1

if x >= sum(a_list):
    print("Yes")
else:
    print("No")

