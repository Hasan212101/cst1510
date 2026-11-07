"""
RECORD CHECK - my version
=========================

Name : Md. Ibne Hasan Rabbi
Lane : AI
Date : 19/10/26

Run it: python template.py
"""

import os

def check_record(value, limit):
    """Calculates difference, percent, and status for a record"""
    diff = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0
    if value > limit:
        status = 'OVER LIMIT'
    else:
        status = 'OK'
    return diff, percent, status

def print_report(label, value, limit, diff, percent, status):
    print(f"Dataset: {label} | Value: {value} | Limit: {limit} | Diff: {diff:.1f} | Percent: {percent:.1f}% | Status: {status}")

def load_records(path):
    """Reads dataset name, value, and limit from a file and returns a list of dicts."""
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, loaded, expected = parts
                    records.append({
                        "label": name,
                        "value": float(loaded),
                        "limit": float(expected)
                    })
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    return records

# ================================================================= SETUP & LOADING
# 1. Determine correct file path dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "survey_records.txt")

# 2. Load records from file
records = load_records(file_path)

# ================================================================= PROCESS + OUTPUT
# 3. Loop over records, call check_record and print_report, and save results
over_limit_count = 0
output_path = os.path.join(script_dir, "results.txt")

with open(output_path, "w") as f:
    for r in records:
        diff, percent, status = check_record(r["value"], r["limit"])
        print_report(r["label"], r["value"], r["limit"], diff, percent, status)
        
        if status == "OVER LIMIT":
            over_limit_count += 1
            
        f.write(f"{r['label']},{status}\n")

print(f"\nTotal OVER LIMIT count: {over_limit_count}")

