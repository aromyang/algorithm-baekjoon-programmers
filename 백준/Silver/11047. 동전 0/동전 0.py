n, k = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)
cnt = 0
for i in l:
    if i > k:
        continue
    cnt += k // i
    k %= i
print(cnt)
