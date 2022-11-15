l = []
for _ in range(5):
    l.append(int(input()))
print(min(l[:3]) + min(l[3:]) - 50)
