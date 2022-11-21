k, n = map(int, input().split())
l = []
for _ in range(k):
    l.append(int(input()))

start = 1
end = max(l)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in l:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
