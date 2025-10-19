a = int(input())
e = []

for i in range(a):
    b, c = input().split()
    d = int(b) + int(c)
    e.append(d)
for e in e[ ::1 ]:
    print(e)
