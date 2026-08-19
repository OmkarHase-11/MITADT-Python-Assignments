# 0/1 Knapsack Problem
# Find the maximum value that can be carried
# without exceeding the given weight capacity.


weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
capacity = 8


#TOP-DOWN

def top_down(i, capacity, memo):

    if i == 0 or capacity == 0:
        return 0

    if memo[i][capacity] != -1:
        return memo[i][capacity]

    # Do not select the current item
    not_take = top_down(i - 1, capacity, memo)

    # Select the current item if it fits
    take = 0

    if weights[i - 1] <= capacity:
        take = values[i - 1] + top_down(
            i - 1,
            capacity - weights[i - 1],
            memo
        )

    memo[i][capacity] = max(take, not_take)

    return memo[i][capacity]


n = len(weights)

memo = [
    [-1] * (capacity + 1)
    for _ in range(n + 1)
]

answer_top = top_down(n, capacity, memo)

print("Top-Down Result:", answer_top)


#BOTTOM-UP

def bottom_up(weights, values, capacity):

    n = len(weights)

    dp = [
        [0] * (capacity + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for current_weight in range(capacity + 1):

            # Ignore the current item
            dp[i][current_weight] = dp[i - 1][current_weight]

            # Take the current item if possible
            if weights[i - 1] <= current_weight:

                take = (
                    values[i - 1]
                    + dp[i - 1][
                        current_weight - weights[i - 1]
                    ]
                )

                dp[i][current_weight] = max(
                    dp[i][current_weight],
                    take
                )

    return dp[n][capacity]


answer_bottom = bottom_up(
    weights,
    values,
    capacity
)

print("Bottom-Up Result:", answer_bottom)
Comment:-
Top-Down Result: 12
Bottom-Up Result: 12
