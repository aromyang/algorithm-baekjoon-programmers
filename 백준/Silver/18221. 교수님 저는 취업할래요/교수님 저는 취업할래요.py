import math
import sys

input = sys.stdin.readline

n = int(input())
l = []
p = []
me = []
cnt = 0

for i in range(n):
    ll = list(map(int, input().split()))
    if 5 in ll:
        p = ([i, ll.index(5)])
    if 2 in ll:
        me = ([i, ll.index(2)])
    l.append(ll)

if math.sqrt((p[0] - me[0]) ** 2 + (p[1] - me[1]) ** 2) < 5:
    cnt = 0
elif p[0] == me[0]:
    for i in range(min(p[1], me[1]), max(p[1], me[1]) + 1):
        if l[p[0]][i] == 1:
            cnt += 1
elif p[1] == me[1]:
    for i in range(min(p[0], me[0]), max([p[0], me[0]]) + 1):
        if l[i][p[1]] == 1:
            cnt += 1
else:
    for i in range(min(p[0], me[0]), max(p[0], me[0]) + 1):
        for j in range(min(p[1], me[1]), max(p[1], me[1]) + 1):
            if l[i][j] == 1:
                cnt += 1

if cnt >= 3:
    print(1)
else:
    print(0)
