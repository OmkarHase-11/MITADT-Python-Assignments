import csv
import json

input_file = "input.csv"
output_file = "output.json"

# Read CSV data
with open(input_file, mode="r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write data to JSON
with open(output_file, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data successfully converted to {output_file}")
