t = int(input())
for _ in range(t):
    l = sorted(map(int, input().split()))
    if l[3] - l[1] >= 4:
        print('KIN')
    else:
        print(sum(l[1:4]))
