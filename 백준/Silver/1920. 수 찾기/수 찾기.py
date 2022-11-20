n = int(input())
l1 = sorted(list(map(int, input().split())))
m = int(input())
l2 = list(map(int, input().split()))


def bs(l, a):
    start = 0
    end = len(l) - 1

    while True:
        mid = (start + end) // 2

        if l[mid] == a:
            print(1)
            break
        elif l[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
        if start > end:
            print(0)
            break


for i in l2:
    bs(l1, i)
