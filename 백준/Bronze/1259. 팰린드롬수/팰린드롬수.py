while True:
    n = input().strip()
    if n == '0':
        break
    else:
        if n == n[::-1]:
            print('yes')
        else:
            print('no')
