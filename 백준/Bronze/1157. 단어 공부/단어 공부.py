l = list(input().upper())
s = list(set(l))
cnt = []

for i in s:
    cnt.append(l.count(i))

if cnt.count(max(cnt)) == 1:
    print(s[cnt.index(max(cnt))])
else:
    print('?')
