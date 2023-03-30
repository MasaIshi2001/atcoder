s = str(input())

a = s[0]
c = s[len(s)-1]
b = ""
for i in range(len(s)):
    if s != 0 and s!= len(s) - 1:
        b += s[i]

if a.isupper() == True and c.isupper() == True and b.isnumeric() == True:
    b = int(b)
    if b >= 100000  and b <= 999999 :
        print("Yes")
        exit()

print("No")

