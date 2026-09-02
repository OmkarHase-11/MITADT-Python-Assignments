def longest_common_substring(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    # dp[i][j] stores the length of the longest common suffix of s1[0...i-1] and s2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0

    return max_length


def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    result = longest_common_substring(str1, str2)
    print(f"Length of the longest common substring: {result}")


if __name__ == "__main__":
    main()
