t = int(input())
for i in range(t):
    r, s = input().split()
    s = str(s)
    for j in s:
        print(int(r)*j, end='')
    print()
