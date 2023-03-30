n,a,b,c,d = (int(x) for x in input().split())

#xxxxx

nagasa = 0
dictXY = {}

dictXY["XX"] = a
dictXY["XY"] = b
dictXY["YX"] = c
dictXY["YY"] = d
tmp = []

if a > 0:
    tmp.append("XX")

if b > 0:
    tmp.append("XY")

if c > 0:
    tmp.append("YX")

if d > 0:
    tmp.append("YY")

retu = []
retu = tmp.pop()

while len(retu) != 0:
    sentou = retu.pop()
    if sentou == "XX":
        dictXY["XX"] = dictXY["XX"] - 1
    elif sentou == "XY":
        dictXY["XY"] = dictXY["XY"] - 1
    elif sentou == "YX":
        dictXY["YX"] = dictXY["YX"] - 1
    elif sentou == "YY":
        dictXY["YY"] = dictXY["YY"] - 1

    if sentou[1] == "X":
        if dictXY["XX"] > 0:
            retu.append("XX")
        if dictXY["XY"] > 0:
            retu.append("XY")



