"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# 
over_limit_count = 0

# 
while True:
    # ==================== 1. Ask the user for your three values. ==================== INPUT
    label = input("Enter dataset name (or type 'quit' to exit): ")
    
    # যদি ইউজার quit লেখে, তবে লুপ ভেঙে বের হয়ে যাবে
    if label.lower() == "quit":
        break
        
    value = float(input("Enter rows loaded: "))
    Limit = float(input("Enter rows expected: "))

    # ==================== 2. Work out the difference and the percentage. ==================== PROCESS
    difference = Limit - value
    percent = (value / Limit) * 100

    # ==================== 3. Decide a status and store it in a variable called status. ====================
    # Typical: 100%+ হলো OVER LIMIT, 90%+ হলো WARNING, অন্যথায় OK
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ==================== 4. Print the report. ==================== OUTPUT
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    
    # 
    print(f"Loaded    : {value:>10.2f}")
    print(f"Expected  : {Limit:>10.2f}")
    print(f"Difference: {difference:>+10.2f}")
    print(f"Percent   : {percent:>10.2f}%")
    print(f"Status    : {status:>10}")
    print("=" * 34)

# 
print()
print(f"Total records that came back OVER LIMIT during session: {over_limit_count}")

# ==================== 5. Before you finish: ====================
#
# [ ] Run it three times with different numbers
# [ ] Run it with a total of 0 and note the error (do not fix it yet)
# [ ] Check every variable name says what it holds