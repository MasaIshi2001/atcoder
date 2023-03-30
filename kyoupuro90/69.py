n,k = (int(x) for x in input().split())

#k*(k-1)*(k-2)**(n-2)が答えの数となる

ans = 0
if k == 1:
    if n == 1:
        print(1)
    else:
        print(0)
elif n == 1:
    print(k%((10**9)+7))
elif n == 2:
    print(k*(k-1)%((10**9)+7))
else: 
    ans = 1
    b = n-2
    a = k-2
    while b != 0:
        if b%2 == 1:
            ans = (ans*a)%((10**9)+7)
        a = (a*a)%((10**9)+7)
        b = b//2
    print(((k*(k-1))%((10**9)+7))*(ans%((10**9)+7)))