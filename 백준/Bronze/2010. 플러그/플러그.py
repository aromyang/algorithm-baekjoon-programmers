import sys
input = sys.stdin.readline

n = int(input())
c = 0
for _ in range(n):
    c += int(input())
print(c - n + 1)
