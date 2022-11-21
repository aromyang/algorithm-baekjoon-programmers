import math


def prime(num):
    if num == 2:
        return num
    if num == 1 or not num & 1:
        return 0
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return num


m, n = map(int, input().split())
for i in range(m, n + 1):
    if prime(i) != 0:
        print(i)
