def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1

    for cur_money in money:
        for i in range(cur_money, n + 1):
            dp[i] += dp[i - cur_money]
    
    return dp[n] % (10**9 + 7)