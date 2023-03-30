x,k = (int(x) for x in input().split())
x_str = str(x)
x_int = int(x)
x_lis = list(x_str)
x_lis.reverse()


for i in range(k):
    if i < len(x_lis):
        if int(x_lis[i]) <= 4:
            x_int = x_int - (10**(i))*(int(x_lis[i]))
        else:
            x_int = x_int + ((10**(i+1)) - (10**(i))*(int(x_lis[i])))
    
        x_str = str(x_int)
        x_lis = list(x_str)
        x_lis.reverse()
    
    
    
x_lis.reverse()
ans = "".join(x_lis)
print(ans)
    
