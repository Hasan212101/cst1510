"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI and Data Science
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================== CLASS ====================
class Record:
    """Represents a record check with label, value, and limit."""
    
    def __init__(self, label, value, limit):
        """Initializes the Record attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns the status based on the percentage."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================== RECORDS ====================
def load_records(path):
    """Loads records from a file and returns a list of Record objects."""
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
                        records.append(Record(label, value, limit))
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found. Starting with an empty list.")
    return records

records = load_records("records.txt")

# If records.txt is not yet created, use fallback instances for testing
if not records:
    records = [
        Record("survey_2026", 1187.0, 1200.0),
        Record("survey_test", 1300.0, 1200.0)
    ]


# ==================== OUTPUT ====================
over_limit_count = 0

for record in records:
    current_status = record.status()
    if current_status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"Loaded    : {record.value:>10.2f}")
    print(f"Expected  : {record.limit:>10.2f}")
    print(f"Status    : {current_status:>10}")
    print("=" * 34)

print()
print(f"Total records that came back OVER LIMIT: {over_limit_count}")

# ==================== 4. Before you finish: ====================
#
# [ ] Run it and check every record's numbers
# [ ] Check r1 and r2 really are independent - change one, print both.
# [ ] Check every method and __init__ has a one-line docstring