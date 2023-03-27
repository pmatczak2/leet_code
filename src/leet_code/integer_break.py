# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those
# integers. Return the maximum product you can get.

def integer_break(n):
    dp = {1 : 1}
    def dfs(num):
        if num in dp:
            return dp[num]
        dp[num] = 0 if num == n else num
        for i in range(1,num):
            val = dfs(i) * dfs(num - i)
            dp[num] = max(dp[num], val)
        return dp[num]
    return dfs(n)

print(integer_break(10))