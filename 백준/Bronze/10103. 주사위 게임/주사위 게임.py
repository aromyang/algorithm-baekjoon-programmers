n = int(input())
a = b = 100
for _ in range(n):
    x, y = map(int, input().split())
    if x < y:
        a -= y
    elif y < x:
        b -= x
print(a)
print(b)
