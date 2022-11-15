t = int(input())
name = []
alco = []
for _ in range(t):
    n = int(input())
    for _ in range(n):
        s, l = map(str, input().split())
        name.append(s)
        alco.append(int(l))
    print(name[alco.index(max(alco))])
