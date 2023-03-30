import math
a,b,c = (int(x) for x in input().split())

if math.log2(a) < b*math.log2(c):
    print("Yes")
else:
    print("No")

#極力比較にはlogを用いない方が良い。誤差のせいで正しく比較できないからである