# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

''' import math

print(math.sqrt(100)) '''

def status_of (percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
       return "Over limit"
    elif percent >= 90 :
       return"Warning"
    else:
        return"ok"

def check(value, limit):
    """Calculate the difference and percentage between value and limit."""
    difference = value - limit
    percent = (value / limit ) * 100
    return difference , percent

def print_report(label, value, limit, difference, percent, status):
    """ prints the report with the given parameters."""
    print(f"\n - Record Check Report -")
    print(f"label   : {label}")
    print(f"value   : {value}")
    print(f"limit   : {limit}")
    print(f"difference : {difference}")
    print(f"percent : {percent}")
    print(f"status   : {status}")
    print("---------------------------")


lable = input('Enter lable (e.g., name , hostname , ip)')
value = (input('Enter value: '))
limit = (input ('Enter limit:'))