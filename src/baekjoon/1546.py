n = int(input())
b = list(map(int, input().split()   ))

m = max(b)

a = (sum(b) / n) / m * 100

print(a)
