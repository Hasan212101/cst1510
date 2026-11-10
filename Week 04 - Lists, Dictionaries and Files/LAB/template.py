"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI and Data Science
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate the difference and percentage between value and limit."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def load_records(path):
    """Loads records from a file and returns a list of dictionaries."""
    records = []
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        label = parts[0].strip()
                        value = float(parts[1].strip())
                        limit = float(parts[2].strip())
                        records.append({"label": label, "value": value, "limit": limit})
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found. Starting with an empty list.")
    return records

def print_report(label, value, limit, difference, percent, status):
    """Prints the report with the given parameters."""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Loaded    : {value:>10.2f}")
    print(f"Expected  : {limit:>10.2f}")
    print(f"Difference: {difference:>+10.2f}")
    print(f"Percent   : {percent:>10.2f}%")
    print(f"Status    : {status:>10}")
    print("=" * 34)

# ==================== 1. Load Records ====================
records = load_records("records.txt")

over_limit_count = 0
output_lines = []

# ==================== 2. Process Records ====================
for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)
    output_lines.append(f"{label},{status}\n")

# ==================== 3. Write Results to File ====================
try:
    with open("results.txt", "w") as outfile:
        outfile.writelines(output_lines)
except Exception as e:
    print(f"Error writing to file: {e}")

print()
print(f"Total records that came back OVER LIMIT: {over_limit_count}")

# ==================== 4. Before you finish: ====================
#
# [ ] Run it and check every record's numbers
# [ ] Try it with a file that does not exist to check try/except
# [ ] Check every function does one job

