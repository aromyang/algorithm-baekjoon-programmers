import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

m = min(a / i, b / j, c / k)
print(a - m * i, b - m * j, c - m * k)
