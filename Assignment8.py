# Open the input file and read all lines
with open("data.txt", "r") as f:
    content = f.readlines()

# Find the total number of lines
total_lines = len(content)

print("Number of lines in the file:", total_lines)

# Get the first two lines
selected_lines = content[:2]

print("\nFirst two lines are:")
for text in selected_lines:
    print(text, end="")

# Save the first two lines into another file
with open("result.txt", "w") as f:
    f.writelines(selected_lines)

print("\n\nThe first two lines were saved in result.txt")
