a,b = (str(x) for x in input().split())
a_lis = list(reversed(list(a)))
b_lis = list(reversed(list(b)))
length = min(len(a),len(b))

for i in range(length):
    wa = int(a_lis[i]) + int(b_lis[i])
    if wa >= 10:
        print("Hard")
        exit()

print("Easy")