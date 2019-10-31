# Library
# tutorial video - https://www.youtube.com/watch?v=La6ZO8vu-1w
import csv, json

csvFilePath = "data.csv"
jsonFilePath = "data.js"

# Read the CSV and add the data to dictionary ...
with open(csvFilePath) as f:
    reader = csv.DictReader(f)
    rows = list(reader)


# Write data to a JSON file ...
with open(jsonFilePath, "w") as f:
    json.dump(rows, f, indent=4)

# Open the Terminal and enter python convertCSVtoJSON.py to complete the conversion. 
# Use General Expression to find  "([^"]+)":  and replace with  $1:  to remove the double quotation on key objects.