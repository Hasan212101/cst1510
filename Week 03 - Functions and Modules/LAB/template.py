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

over_limit_count = 0

while True:
    # ==================== 1. Ask the user for your three values. ==================== INPUT
    label = input("Enter dataset name (or type 'quit' to exit): ")
    
    if label.lower() == "quit":
        break
        
    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))

    # ==================== 2. Work out the difference, percentage, and status. ==================== PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # ==================== 3. Print the report. ==================== OUTPUT
    print_report(label, value, limit, difference, percent, status)

print()
print(f"Total records that came back OVER LIMIT during session: {over_limit_count}")

# ==================== 4. Before you finish: ====================
#
# [ ] Run it three times with different numbers
# [ ] Run it with a total of 0 and note the error (do not fix it yet)
# [ ] Check every function does one job - if a function both calculates and prints, split it
