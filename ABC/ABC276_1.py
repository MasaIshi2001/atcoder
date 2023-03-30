s = input()
pos = -1
for i in range(len(s)):
    if s[i] == "a":
        pos = i+1

print(pos)