H, M = input().split()
P = int(input())
H = int(H) + int(P / 60)
H = H % 24
P = P % 60

if int(M) + P < 60:
    print(int(H), int(M) + P)
elif int(M) + P >= 60:
    if int(H) + ((int(M) + P) // 60) > 23:
        print(int(H) - 23, int(M) + P - 60 * ((int(M) + P) // 60))
    else:
        print(int(H) + ((int(M) + P) // 60), int(M) + P - 60 * ((int(M) + P) // 60))
