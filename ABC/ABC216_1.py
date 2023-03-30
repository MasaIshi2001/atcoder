s = list(str(input()))
idx = s.index(".")
if 0<= int(s[idx+1]) <=2:
    print("".join(s[0:idx])+"-")
elif 3<= int(s[idx+1]) <=6:
    print("".join(s[0:idx]))
else:
    print("".join(s[0:idx])+"+")
