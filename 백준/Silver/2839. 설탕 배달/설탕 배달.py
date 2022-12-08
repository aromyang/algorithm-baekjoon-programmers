def sol(n):
    if n % 5 == 0:
        return n // 5
    else:
        nn = n - 3
        while nn > 0:
            if nn % 5 == 0:
                return (n - nn) // 3 + (nn // 5)
            nn -= 3

    return n // 3 if n % 3 == 0 else -1


print(sol(int(input())))
