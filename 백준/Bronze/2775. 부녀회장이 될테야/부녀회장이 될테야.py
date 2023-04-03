def get_people(k, n):
    if k == 1:
        return n * (n + 1) // 2
    if n == 0:
        return 0
    return get_people(k, n - 1) + get_people(k - 1, n)


t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    print(get_people(k, n))