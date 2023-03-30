abc = str(input())
a1 = int(abc[0]*100+abc[1]*10+abc[2])
a2 = int(abc[1]*100+abc[2]*10+abc[0])
a3 = int(abc[2]*100+abc[0]*10+abc[1])

print(a1 + a2+a3)
