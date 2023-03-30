import math

def factorization(n):
    arr = []
    temp = n
    if temp < 3*10**9:
        for i in range(2, 3*10**9):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                    if cnt == 2:
                        break
                arr.append([i, cnt])
                if cnt == 2:
                    break

        if temp!=1:
            arr.append([temp, 1])

        if arr==[]:
            arr.append([n, 1])
    else:
        for i in range(3*10**9,2,-1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])
                if cnt == 2:
                    break

        if temp!=1:
            arr.append([temp, 1])

        if arr==[]:
            arr.append([n, 1])

    return arr

# def eratosthenes2(n):
#     is_prime = ([False, True] * (n//2+1))[0: n+1]
#     is_prime[1] = False
#     is_prime[2] = True
#     for i in range(3, n+1, 2):
#         if not(is_prime[i]):
#             continue
#         if i*i > n:
#             break
#         for k in range(i*i, n+1, i):
#             is_prime[k] = False
#     return is_prime

# def eratosthenes2(N):
#     A=list(range(2,N+1))
#     p=list()
#     while A[0]**2<=N:
#         tmp=A[0]
#         p.append(tmp)
#         A=[e for e in A if e%tmp!=0]
#     return p + A
    

t = int(input())
test = []
for i in range(t):
    n = int(input())
    test.append(n)

ans = []
e = []
for i in test:
    #e = eratosthenes2(i)
    s = factorization(i)
    ans.append(s)

for i in ans:
    i = sorted(i, key=lambda x:x[1], reverse=True)
    for j in i:
      print(j[0], end=" ")
    print()