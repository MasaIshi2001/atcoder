import math

a,b = (int(x) for x in input().split())
hosei = 1/math.sqrt(a**2+b**2)
new_a = hosei*a
new_b = hosei*b

print(str(new_a)+" "+str(new_b))