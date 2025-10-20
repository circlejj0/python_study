n = int(input())
d = []

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        e = 10000 + a * 1000
        d.append(e)
    elif a == b or a == c:
        f = 1000 + a * 100
        d.append(f)
    elif b == c:
        g = 1000 + b * 100
        d.append(g)
    else:
        i = max(a, b, c) * 100
        d.append(i)
j = max(d)
print(j)
