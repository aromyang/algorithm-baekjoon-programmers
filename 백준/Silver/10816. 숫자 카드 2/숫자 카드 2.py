import sys
input = sys.stdin.readline

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

cnt = {}
for i in l1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in l2:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
        