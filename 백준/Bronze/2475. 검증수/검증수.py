l = list(map(int, input().split()))

an = 0
for i in l:
    an += i ** 2
print(an % 10)
