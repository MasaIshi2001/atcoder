n,k,q = (int(x) for x in input().split())
A_list = list(map(int,input().split()))
L_list = list(map(int,input().split()))

for i in L_list:
    if A_list[i-1]+1 not in A_list:
        if A_list[i-1]+1 <= n:
            A_list[i-1] = A_list[i-1] + 1

print(*A_list)
        