n = int(input())

if n == 1:
    print(1)
else:
    cnt = 2
    start = 2
    end = start + (cnt - 1) * 6 - 1
    while True:
        if start <= n <= end:
            print(cnt)
            break
        else:
            start = end + 1
            end = start + cnt * 6 - 1
            cnt += 1