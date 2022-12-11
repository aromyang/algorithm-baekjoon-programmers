def solution(price, money, count):
    s = 0
    for i in range(1, count + 1):
        s += (i * price)
    
    return s - money if money < s else 0