n = int(input())
lis = list(map(str,input().split()))

if "and" in lis:
    print("Yes")
elif "not" in lis:
    print("Yes")
elif "that" in lis:
    print("Yes")
elif "you" in lis:
    print("Yes")
elif "the" in lis:
    print("Yes")
else:
    print("No")