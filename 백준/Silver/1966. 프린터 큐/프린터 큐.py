t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    ori = list(map(int, input().split()))
    queue = []
    for i, o in enumerate(ori):
        queue.append((i, o))

    an = 0
    while queue:
        high = max(ori)
        now = queue.pop(0)
        if now[1] >= high:
            ori.remove(high)
            an += 1
            if now[0] == target:
                print(an)
                queue.clear()
        else:
            queue.append(now)




