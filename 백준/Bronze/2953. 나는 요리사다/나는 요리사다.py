a = 0
b = 0
for i in range(5):
    score = list(map(int, input().split()))
    if sum(score) > b:
        b = sum(score)
        a = i + 1
print(a, b)
