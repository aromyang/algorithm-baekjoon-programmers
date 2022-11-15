n = int(input())
for i in range(1, n * 2):
    if i == n:
        print('*' * n)
    elif i > n:
        print('*' * (n * 2 - i))
    else:
        print('*' * i)
