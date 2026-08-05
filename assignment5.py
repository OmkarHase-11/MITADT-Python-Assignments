# Program to find the Longest Common Subsequence (LCS)
# using Dynamic Programming

def find_lcs(first, second):
    rows = len(first)
    cols = len(second)

    # Create a DP table filled with zeros
    table = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Build the DP table
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if first[r - 1] == second[c - 1]:
                table[r][c] = table[r - 1][c - 1] + 1
            else:
                table[r][c] = max(table[r - 1][c], table[r][c - 1])

    # Trace back to find the LCS
    r = rows
    c = cols
    result = []

    while r > 0 and c > 0:
        if first[r - 1] == second[c - 1]:
            result.append(first[r - 1])
            r -= 1
            c -= 1
        elif table[r - 1][c] >= table[r][c - 1]:
            r -= 1
        else:
            c -= 1

    result.reverse()

    return "".join(result), table[rows][cols]


# Main Program
seq1 = "Omkar"
seq2 = "Hase"

subsequence, lcs_length = find_lcs(seq1, seq2)

print("First Sequence:", seq1)
print("Second Sequence:", seq2)
print("\nLongest Common Subsequence:", subsequence)
print("Length of LCS:", lcs_length)