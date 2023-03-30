n = str(input())
n_lis = list(n)
nIdx = n_lis.index(".")
if n_lis[nIdx+1] <= 4:
    print("".join(n_lis[0:nIdx]))
else:
    num = int("".join(n_lis[0:nIdx])) + 1
    print(num)
    

