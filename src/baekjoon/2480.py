a, b, c = input().split()

if int(a) == int(b) == int(c):
    print(10000 + int(a) * 1000)
elif int(a) == int(b):
    print(1000 + int(a) * 100)
elif int(b) == int(c):
    print(1000 + int(b) * 100)
elif int(a) == int(c):
    print(1000 + int(a) * 100)
elif int(a) != int(b) != int(c):
    print(max(int(a), int(b), int(c)) * 100)
