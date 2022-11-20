n = int(input())
length = len(str(n))
start = n - 9 * length
an = 0

for i in range(start, n):
    sum = i
    for j in str(i):
        if '-' in j:
            continue
        else:
            sum += int(j)
    if sum == n:
        an = i
        break

print(an)


