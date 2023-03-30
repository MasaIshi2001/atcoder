n,x,y = (int(x) for x in input().split())
 
red = [0 for i in range(n)]
blue = [0 for j in range(n)]
 
red[n-1] = 1
now = n-1
while now > 0:
    red[now - 1] += red[now]
    blue[now] += x*red[now]
    red[now] = 0
 
    red[now - 1] += blue[now]
    blue[now - 1] += y*blue[now]
    blue[now] = 0
 
    now = now - 1
    
print(blue[0])