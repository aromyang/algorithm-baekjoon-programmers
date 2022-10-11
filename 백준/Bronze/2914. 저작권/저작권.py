import math

a, i = map(int, input().split())
i = (i - 1) + 0.01
print(math.ceil(a * i))
