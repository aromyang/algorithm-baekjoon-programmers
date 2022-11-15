t = int(input())
for _ in range(t):
    y = k = 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        print('Yonsei')
    elif k > y:
        print('korea')
    else:
        print('Draw')
