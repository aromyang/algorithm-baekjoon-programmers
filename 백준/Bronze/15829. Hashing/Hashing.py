l = int(input())
s = input()

alpha = "abcdefghijklmnopqrstuvwxyz"
an = 0

for i, ss in enumerate(s):
    idx = alpha.find(ss) + 1
    an += (idx * (31 ** i))

print(an % 1234567891)

