k, n, m = map(int, input().split())

if k * n > m:
    print(k * n - m)
elif k * n <= m:
    print(0)
