H, M = input().split()
0 <= int(H) <= 24, 0 <= int(M) <= 60
if int(M) - 45 >= 0:
    print(int(H), int(M) - 45)
elif int(M) - 45 < 0:
    if int(H) - 1 < 0:
        print(23, int(M) + 15)
    else:
        print(int(H) - 1, int(M) + 15)
