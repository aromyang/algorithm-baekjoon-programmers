l = []
for _ in range(9):
    l.append(int(input()))
l.sort()
s = sum(l)
for i in range(9):
    for j in range(i + 1, 9):
        a = l[i]
        b = l[j]
        if s - a - b == 100:
            l.remove(a)
            l.remove(b)
            break
    if len(l) == 7:
        break
for i in l:
    print(i)
