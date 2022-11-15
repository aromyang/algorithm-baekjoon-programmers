t = int(input())
for _ in range(t):
    p, m = map(int, input().split())
    l = []
    count = 0
    for _ in range(p):
        i = int(input())
        if i in l:
            count += 1
        else:
            l.append(i)
    print(count)
    