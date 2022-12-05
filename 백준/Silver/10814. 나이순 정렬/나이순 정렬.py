n = int(input())
l = []
for _ in range(n):
    age, name = map(str, input().split())
    l.append((int(age), name))
l.sort(key=lambda x: x[0])

for i in l:
    print(i[0], i[1])
