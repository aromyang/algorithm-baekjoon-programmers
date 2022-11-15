k = int(input())
for i in range(k):
    l = list(map(int, input().split()))
    del l[0]
    l.sort(reverse=True)
    print('Class', i+1)
    g = l[0] - l[1]
    for j in range(1, len(l)-1):
        if l[j] - l[j+1] > g:
            g = l[j] - l[j+1]
    print('Max {}, Min {}, Largest gap {}'.format(l[0], l[-1], g))
