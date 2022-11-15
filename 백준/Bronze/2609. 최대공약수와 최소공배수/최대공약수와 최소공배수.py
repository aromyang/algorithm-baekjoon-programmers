def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x


a, b = map(int, input().split())
print(gcd(a, b))
print((a * b) // gcd(a, b))
