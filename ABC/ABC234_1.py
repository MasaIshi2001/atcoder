n = int(input())
f1 = n**2+2*n+3
f2 = f1**2+2*f1+3
f2x = (f1+n)**2+2*(f1+n)+3
f3 = (f2+f2x)**2+2*(f2+f2x)+3
print(f3)