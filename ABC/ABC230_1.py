n = int(input())
if n < 42:
    n1 = str(n)
    print("AGC"+ n.zfill(3))
else:
    n1 = str(n+1)
    print("AGC"+ n.zfill(3))