n = int(input())
r = int(0)

while n >= 0:
    r += n
    n = n - 1
    if n == 0:
        print(r)
