s = 'abcdefghijklmnopqrstuvwxyz'
w = input()
for i in s:
    if i in w:
        print(w.index(i), end=' ')
    else:
        print(-1, end=' ')
