l = []
for _ in range(5):
    l.append(int(input()))
print(sum(l) // 5)
l.sort()
print(l[2])
