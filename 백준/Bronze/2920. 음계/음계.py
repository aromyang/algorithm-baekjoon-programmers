l = list(map(int, input().split()))
if sorted(l) == l:
    print('ascending')
elif sorted(l, reverse=True) == l:
    print('descending')
else:
    print('mixed')
