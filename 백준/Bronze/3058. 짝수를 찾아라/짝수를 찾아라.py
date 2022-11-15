t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    l2 = []
    for n in l:
        if not n & 1:
            l2.append(n)
    print(sum(l2), min(l2))
