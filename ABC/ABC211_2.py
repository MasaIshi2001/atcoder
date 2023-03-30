s_lis = ["" for i in range(4)]
for i in range(4):
    s_lis[i] = input()

if s_lis.count("H") == 1:
    if s_lis.count("2B") == 1:
        if s_lis.count("3B") == 1:
            if s_lis.count("HR") == 1:
                print("Yes")
                exit()
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
