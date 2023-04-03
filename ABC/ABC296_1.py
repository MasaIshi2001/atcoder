n = int(input())
s = str(input())

for i in range(len(s)):
    if i >= 1:
        if past == "M":
            if s[i] == "M":
                print("No")
                exit()
        elif past == "S":
            if s[i] == "S":
                print("No")
                exit()

    past = s[i]

print("Yes")