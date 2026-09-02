def climb_stairs(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # dp[i] stores the number of ways to reach stair i
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    try:
        n = int(input("Enter the number of stairs: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        total_ways = climb_stairs(n)
        print(f"Total number of distinct ways to climb {n} stairs: {total_ways}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
