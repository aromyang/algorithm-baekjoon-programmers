import sys

input = sys.stdin.readline

n = int(input())
w = 0

for _ in range(n):
    a, b = map(str, input().strip().split())
    h, m = map(int, a.split(':'))
    t = int(b)
    if 7 <= h <= 18:
        if m + t >= 60 and h == 18:
            w += ((10 * (60 - m)) + 5 * (t - (60 - m)))
        else:
            w += (10 * t)
    else:
        if m + t >= 60 and h == 6:
            w += ((5 * (60 - m)) + 10 * (t - (60 - m)))
        else:
            w += (5 * t)

print(w)
