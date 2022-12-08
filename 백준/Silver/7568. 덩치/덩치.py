n = int(input())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

an = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if p[j][0] > p[i][0] and p[j][1] > p[i][1]:
            cnt += 1
    an.append(cnt + 1)


print(*an)
