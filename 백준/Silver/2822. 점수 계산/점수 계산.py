l = []
l2 = []
for _ in range(8):
    l.append(int(input()))
new = sorted(l, reverse=True)
print(sum(new[:5]))
for i in range(5):
    l2.append(l.index(new[i]) + 1)
l2.sort()
print(*l2)
