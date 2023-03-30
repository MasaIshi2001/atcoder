A_lis = [["R","G","B"],["G","B","R"],["B","R","G"]]

s = list(map(str,input().split()))
t = list(map(str,input().split()))

if (s in A_lis) == (t in A_lis):
    print("Yes")
else:
    print("No")