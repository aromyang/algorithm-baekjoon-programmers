t = int(input())

for _ in range(t):
    an = ''
    h, w, n = map(int, input().split())
    if n % h == 0:
        an += str(h)
    else:
        an += str(n % h)
    if h * (n//h) < n:
        num = n//h + 1
    else:
        num = n // h
    if num < 10:
        an += ('0' + str(num))
    else:
        an += str(num)
    print(an)
