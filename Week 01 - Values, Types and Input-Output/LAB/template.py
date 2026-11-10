"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI / Data Science
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================== 1. Ask the user for your three values. ==================== INPUT
#
#  - the first is TEXT      (dataset name) -> no conversion needed
#  - the second is a NUMBER (rows loaded - use float(), not int())
#  - the third is a NUMBER  (rows expected - use float(), not int())
#
#  Remember: input() always gives back text.

label = input("Enter dataset name: ")
first = float(input("Enter rows loaded: "))
second = float(input("Enter rows expected: "))

# ==================== 2. Work out what you were NOT given. ==================== PROCESS
#
#  - difference : how far the first is from the second (e.g., missing rows)
#  - percent    : the first as a percentage of the second
#  - deficit_ratio : an extra calculated line for data tracking
#
#  Do not type the answers. Calculate them.

difference = second - first
percent = (first / second) * 100
deficit_ratio = difference / second  # Useful extra calculation for AI data tracking

# ==================== 3. Print the report. ==================== OUTPUT
#
#  Threshold : print the three values you were given, inside a border
#  Typical   : add difference and percent, 2 decimal places, right-aligned
#  Excellent : difference always shows its sign, plus one line of your own
#
#  Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#            f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f" RECORD CHECK - {label}")
print("=" * 34)

# Your report lines go here
print(f"Loaded    : {first:>10.2f}")
print(f"Expected  : {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"Percent   : {percent:>10.2f}%")
print(f"Deficit   : {deficit_ratio:>+10.2f} (Ratio of missing data)")

print("=" * 34)

# ==================== 4. Before you finish: ====================
#
# [ ] Run it three times with different numbers
# [ ] Run it with a total of 0 and write the error in your journal
# [ ] Check every variable name says what it holds
# [ ] Show it to the person next to you