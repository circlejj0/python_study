a, b, c = map(int, input().split())

if a >= b:
    if a <= c:
        print(a)
    elif a >= c and b >= c:
        print(b)
    elif a >= c and b <= c:
        print(c)
elif a < b:
    if b <= c:
        print(b)
    elif b >= c and a >= c:
        print(a)
    elif b >= c and a <= c:
        print(c)
else:
    print(a)
