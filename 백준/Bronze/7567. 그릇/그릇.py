l = list(input())
h = 0
a = ''
for i in l:
    if a != i:
        h += 10
    else:
        h += 5
    a = i
print(h)
