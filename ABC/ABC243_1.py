v,a,b,c = (int(x) for x in input().split())

goukei = a + b + c

amari = v % goukei

if amari >= 0 and amari < a:
    print("F")
elif amari >= a and amari < a + b:
    print("M")
elif amari >= a + b and amari < goukei:
    print("T")