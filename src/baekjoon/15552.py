T = int(input())
t = []

for i in range(T):
    a, b = input().split()
    c = int(a) + int(b)
    t.append(c)
for t in t[ ::1 ]:
    print(t)
