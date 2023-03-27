# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those
# integers. Return the maximum product you can get.

def integer_breaker(n):
    dp = {1: 1}  # cashing technique

    def dfs(num):
        if num in dp:  # this can't be further broken down
            return dp[num]

        dp[num] = 0 if num == n else num  # here I am making sure that the original value will be broken down, but the
        # sub problems don't have to be broken down they can be set to the values themselves
        for i in range(1, num):  # loop to determine how you will brake the num
            val = dfs(i) * dfs(num - i)  # multiply left with the right value, need both of their portions to add up
            # to the original which is num
            dp[num] = max(dp[num], val)  # result always to the maximum
        return dp[num]

    return dfs(n)


print(integer_breaker(10))
