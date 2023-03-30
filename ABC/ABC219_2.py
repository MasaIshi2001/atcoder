s1 = str(input())
s2 = str(input())
s3 = str(input())
t = str(input())

t_lis = list(t)

ans = ""
for i in t_lis:
    if i == "1":
        ans = ans + s1
    elif i == "2":
        ans = ans + s2
    elif i == "3":
        ans = ans + s3

print(ans)