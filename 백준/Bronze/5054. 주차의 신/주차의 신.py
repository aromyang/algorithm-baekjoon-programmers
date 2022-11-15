t = int(input())
for _ in range(t):
    a = int(input())
    l = sorted(map(int, input().split()))
    print((l[-1] - l[0]) * 2)
