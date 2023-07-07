croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ans = 0
word = input()
for c in croatia:
    word = word.replace(c, 'x')

print(len(word))
