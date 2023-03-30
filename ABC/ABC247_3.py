n = int(input())

ans_line = ''
for i in range(n):
    ans_line = ans_line + " " + str(i+1) + " " + ans_line

print(ans_line)