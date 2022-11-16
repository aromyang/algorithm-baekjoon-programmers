import sys

input = sys.stdin.readline

n = int(input())
a = n
cnt = 0

while True:
    a = ((a % 10) * 10) + ((a // 10 + a % 10) % 10)
    cnt += 1
    if a == n:
        break

print(cnt)
