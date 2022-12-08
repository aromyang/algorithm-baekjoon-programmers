import sys
input = sys.stdin.readline

n = int(input().strip())
dots = []
for i in range(n):
    x, y = map(int, input().strip().split())
    dots.append((x, y))
dots.sort(key=lambda k: (k[1], k[0]))

for i in dots:
    print(i[0], i[1])
