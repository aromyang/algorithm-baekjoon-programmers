n = int(input())
l = []
for _ in range(n):
    n, d, m, y = input().split()
    l.append((int(y), int(m), int(d), n))
l.sort()
print(l[-1][3])
print(l[0][3])
