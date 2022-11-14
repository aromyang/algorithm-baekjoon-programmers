result = [i + 1 for i in range(20)]
for _ in range(10):
    a, b = map(int, input().split())
    result[a - 1:b] = result[a - 1:b][::-1]

print(*result)