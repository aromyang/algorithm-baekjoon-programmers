import sys

input = sys.stdin.readline


def f(x, y):
    return (x + y) * (x - y)


a, b = map(int, input().split())
print(f(a, b))
