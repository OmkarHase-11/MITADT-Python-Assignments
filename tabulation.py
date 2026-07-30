from functools import lru_cache


# Memoization / Top-Down Approach
@lru_cache(maxsize=None)
def fibonacci_memoization(n):
    if n <= 1:
        return n

    return (
        fibonacci_memoization(n - 1)
        + fibonacci_memoization(n - 2)
    )


# Tabulation / Bottom-Up Approach
def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0, 1]

    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


# Main Program
try:
    n = int(input("Enter the value of n: "))

    if n < 0:
        print("Please enter a non-negative integer.")

    else:
        memo_result = fibonacci_memoization(n)
        table_result = fibonacci_tabulation(n)

        print("\n--- Fibonacci Result ---")
        print("Value of n:", n)
        print("Using Memoization:", memo_result)
        print("Using Tabulation :", table_result)

except ValueError:
    print("Invalid input. Please enter an integer.")
