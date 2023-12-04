# Here are some simple examples of bottom-up and top-down DP solutions
# for the same problem (factorial)
# The factorial of n, n!, which I'm going to refer to as `F(n)`
# can be defined by the recurrence `F(n) = n * F(n-1)`, `F(0) = 1`
# Which is a basic problem that can naturally be solved with recursion


def factorial_topdown(n):
    if n <= 0:
        return 1
    else:
        return factorial_topdown(n - 1) * n


def factorial_bottomup(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i

    return dp[n]


print("Top-Down:", factorial_topdown(20))
print()
print("Bottom-Up:", factorial_bottomup(20))
