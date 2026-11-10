"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI and Data Science
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================== LOAD ====================
# 1. Read your data file with pd.read_csv()
df = pd.read_csv("records.csv")


# ==================== PROCESS ====================
# 2. Add a "percent" column and a "status" column using apply() with a lambda
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ==================== OUTPUT ====================
# 3. Print the DataFrame, filter non-OK rows, group by status, and save outputs
print("--- Full DataFrame with Percent and Status ---")
print(df)
print()

# Filter rows where status is not "OK"
filtered_df = df[df["status"] != "OK"]
print("--- Records that require attention (Not OK) ---")
print(filtered_df)
print()

# Group by status and print counts
status_counts = df.groupby("status").size()
print("--- Counts per Status ---")
print(status_counts)

# Save the full DataFrame to a new CSV
df.to_csv("results_summary.csv", index=False)

# ==================== 4. Before you finish: ====================
#
# [ ] Run it and check the percent/status columns by hand for one row
# [ ] Check you used & (not "and") if you combined more than one condition
# [ ] Check every column your code refers to actually exists - watch case