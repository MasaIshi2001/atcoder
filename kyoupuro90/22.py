import math
from decimal import Decimal, getcontext

a,b,c = (Decimal(x) for x in input().split())

henLen1 = math.gcd(int(a),int(b))
henLen2 = math.gcd(int(a),int(c))
henLen = math.gcd(henLen1,henLen2)

cutCnt = 0

cutCnt = math.floor((a/henLen - 1) + (b/henLen - 1) + (c/henLen - 1))
getcontext().prec = 19

print(cutCnt)