def fibo(n):
    fi = [0, 1, 1]
    for i in range(3, n + 1):
        fi.append(fi[i - 1] + fi[i - 2])
    return fi


n = int(input())
if n == 0:
    print(0)
else:
    print(fibo(n)[-1])
