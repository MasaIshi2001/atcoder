n = int(input())

bin_n = bin(n)[2:]
bin_n = list(bin_n)

ans = ""
for i in range(len(bin_n)):
    if bin_n[i] == "0":
        if i != len(bin_n) - 1:
            ans = ans + "B"

    elif bin_n[i] == "1":
        if i == len(bin_n) - 1:
            ans = ans + "A"
        else:
            ans = ans + "A"
            ans = ans + "B"

print(ans)
        


