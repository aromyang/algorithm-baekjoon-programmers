import sys

input = sys.stdin.readline

n = int(input())
l = sorted(map(int, input().split()))
p = 0

for i in range(n):
    if l[i] >= n - i:
        p = 1
        print(n - i)
        break
if p != 1:
    print(0)