n = int(input())
s = str(input())
s = list(s)
for i in range(len(s)):
    if s[i] == "1":
        if i%2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
