t = int(input())
for _ in range(t):
    a = int(input())
    index = 0
    while a > 0:
        if a % 2 == 1:
            print(index, end=' ')
        a //= 2
        index += 1
            