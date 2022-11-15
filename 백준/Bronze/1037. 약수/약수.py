n = int(input())
if n == 1:
    print(int(input()) ** 2)
else:
    l = sorted(map(int, input().split()))
    print(l[0] * l[-1])
