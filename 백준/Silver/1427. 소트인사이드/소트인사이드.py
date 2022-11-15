l = list(map(int, str(input())))
l.sort(reverse=True)
for i in l:
    print(i, end='')
    