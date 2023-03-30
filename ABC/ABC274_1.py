from decimal import Decimal,ROUND_HALF_UP
a,b = (int(x) for x in input().split())
print(Decimal(str(a/b)).quantize('0.001',rounding=ROUND_HALF_UP))
