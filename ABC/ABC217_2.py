s1 = input()
s2 = input()
s3 = input()

ans_lis = ["ABC" , "ARC" , "AGC" , "AHC"]
s_lis = [s1,s2,s3]
diff_lis = set(ans_lis)^set(s_lis)

print(diff_lis[0])