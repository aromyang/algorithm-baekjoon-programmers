import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())
max = max(x, y)
min = min(x, y)
an = 0

if w * 4 < s * 2:
    an = (x + y) * w
else:
    an = min * s
    if w <= s:
        an += ((max - min) * w)
    else:
        if (max - min) & 1:
            an += ((max - min - 1) * s + w)
        else:
            an += ((max - min) * s)
print(an)
