t = int(input())
l = [300, 60, 10]

if t % 10 != 0:
    print(-1)
else:
    for i in l:
        print(t//i, end=' ')
        t %= i
