import sys

input = sys.stdin.readline

t = int(input())
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(t):
    a = input().strip()
    b = input().strip()
    c = ''
    for i in range(len(a)):
        if a[i] == ' ':
            c += ' '
        else:
            c += b[s.index(a[i])]
    print(c)
