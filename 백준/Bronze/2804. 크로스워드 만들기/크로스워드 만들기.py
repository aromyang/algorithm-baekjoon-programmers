import sys
input = sys.stdin.readline

a, b = map(list, input().split())

for i in range(len(a)):
    if a[i] in b:
        aa = b.index(a[i])
        bb = i
        break

for i in range(len(b)):
    if i == aa:
        print(''.join(a))
    else:
        print('.' * bb + b[i] + '.' * (len(a) - bb - 1))
