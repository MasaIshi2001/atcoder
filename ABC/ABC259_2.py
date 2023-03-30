import math
a,b,d = (int(x) for x in input().split())

x = math.cos(math.radians(d))*a - math.sin(math.radians(d))*b
y = math.sin(math.radians(d))*a - math.cos(math.radians(d))*b

print(x + " " + y)
