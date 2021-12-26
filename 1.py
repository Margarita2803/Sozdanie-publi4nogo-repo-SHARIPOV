a = []
while True:
    x = int(input())
    if x % 2 == 0 and x != 0:
        a.append(x)
    if x == '0':
        break
    print(a)
