n, m = map(int, input().split())
l = list(map(int, input().split()))
an = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = l[i] + l[j] + l[k]
            if sum > m:
                continue
            else:
                an = max(an, sum)

print(an)
