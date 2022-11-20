import math

n = int(input())
l = list(map(int, input().split()))


def prime(num):
    if num == 2:
        return 1
    if num == 1 or not num & 1:
        return 0
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


cnt = 0
for j in l:
    if prime(j):
        cnt += 1

print(cnt)
