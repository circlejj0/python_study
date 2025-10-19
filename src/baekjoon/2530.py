a, b, c = input().split()
d = int(input())

if d + int(c) >= 60:
    e = (d + int(c)) // 60
    f = (d + int(c)) % 60
    if int(b) + int(e) >= 60:
        g = (int(b) + int(e)) // 60
        h = (int(b) + int(e)) % 60
        if int(a) + int(g) >= 24:
            i = (int(a) + int(g)) % 24
            print(i, h, f)
        else:
            print(int(a) + int(g), h, f)
    else:
        print(int(a), int(b) + int(e), f)
else:
    print(int(a), int(b), int(c) + d)
