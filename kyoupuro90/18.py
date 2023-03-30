import math
t = int(input())
l,x,y = (int(x) for x in input().split())
q = int(input())
e_lis = []
for i in range(q):
    e = int(input())
    e_lis.append(e)

temp_kaku = (4*90)/t #1分あたりに回転する角度
zahyou_lis = []

for i in e_lis:
    kakudo = math.radians(temp_kaku *i)
    zahyou_lis.append([0,-l*math.sin(kakudo)/2,-l*math.cos(kakudo)/2+l/2])

for i in zahyou_lis:
    xy_dis = math.sqrt((x-i[0])**2+(y-i[1])**2)
    print(math.degrees(math.atan(i[3]/xy_dis)))