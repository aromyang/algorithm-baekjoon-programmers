w = list(input())
answer = 1
for i in range(len(w) // 2):
    s = w[i]
    e = w[len(w) - i - 1]
    if s != e:
        answer = 0
        break
print(answer)

