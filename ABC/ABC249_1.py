import math
A,B,C,D,E,F,X = (int(x) for x in input().split()) 

set_time_t = math.floor(X/(A+C))
amari_time_t = X%(A+C)

set_time_a = math.floor(X/(D+F))
amari_time_a = X%(D+F)

t_dist = A*B*set_time_t 
a_dist = D*E*set_time_a

if amari_time_t >= A:
    t_dist =  t_dist + A*B
else:
    t_dist = t_dist + amari_time_t*B

if amari_time_a >= D:
    a_dist = a_dist + D*E
else:
    a_dist = a_dist + amari_time_a*E

if t_dist > a_dist:
    print("Takahashi")
elif t_dist < a_dist:
    print("Aoki")
else:
    print("Draw")