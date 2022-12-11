def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x


def solution(n, m):
    g = gcd(n, m)
    l = n * m // g
    return [g, l]
