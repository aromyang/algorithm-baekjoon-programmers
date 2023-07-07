N = int(input())
ans = 0

for _ in range(N):
    word = input()
    exists = set()
    cur = ''
    valid = True
    for w in word:
        if w != cur and w in exists:
            valid = False
            break
        else:
            cur = w
            exists.add(w)
    ans = ans + 1 if valid else ans

print(ans)