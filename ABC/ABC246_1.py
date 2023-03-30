
x1,y1 =(int(x) for x in input().split())
x2,y2 =(int(x) for x in input().split())
x3,y3 =(int(x) for x in input().split())

x_list = [x1,x2,x3]
y_list = [y1,y2,y3]

x_set = list(set(x_list))
y_set = list(set(y_list))

print(2*sum(x_set)-sum(x_list),end=' ')
print(2*sum(y_set)-sum(y_list))