X = int(input())
N = int(input())
r = int(0)

for N in range(N):
    a, b = input().split()
    c = int(a) * int(b)
    r += int(c)

if X == int(r):
        print("Yes")
else:
        print("No")
