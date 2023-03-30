n = int(input())
a_list = []
for i in range(n):
    a_line = list(map(int,input().split()))
    a_list.append(a_line)

#(a1,a2,...aN)と(b1,b2,...,bN)の要素全て掛け合わせ足すということは
#a1*b1+a1*b2+...+aN*bN = (b1+b2+...bN)*a1+... = (b1+b2+...bN)*(a1+a2+...aN)となることを利用する

ans = 1
for i in a_list:
    ans *= sum(i)
    ans = ans % ((10**9)+7)

print(ans)
