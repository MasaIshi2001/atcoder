import math
y = int(input())
m = int(input())
d = int(input())
#step1 past day until hikisuu
day1 = 0
if m == 1:
    y = y - 1 
    m = 13
elif m == 2:
    y = y - 1
    m = 14

k2 = int(math.floor(y/4))
k3 = int(math.floor(y/100))
k4 = int(math.floor(y/400))
k5 = math.floor(306*(m+1)/10)
day1 = 365*y + k2 - k3 + k4 + k5 + d - 429

#step2
day2 = 0
y = 2014
m = 5
d = 17
day2 = 365*y + int(math.floor(y/4)) - int(math.floor(y/100)) + int(math.floor(y/400)) + int(math.floor(306*(m+1)/10)) + d - 429


print(day2-day1)