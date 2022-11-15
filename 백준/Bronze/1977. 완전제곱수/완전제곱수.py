import math

m = int(input())
n = int(input())
l = []
for i in range(m, n+1):
    if math.sqrt(i).is_integer():
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
