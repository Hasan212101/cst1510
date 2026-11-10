"""
RECORD CHECK - my version

Name : MD. IBNE HASAN RABBI
Lane : AI and Data Science
Date : 

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================== FUNCTIONS ====================
def parse_line(raw_line):
    """Cleans and parses one raw, messy line into a dictionary with clean keys and values."""
    # Remove leading/trailing whitespaces and convert to lowercase
    cleaned_line = raw_line.strip().lower()
    
    # Split by comma to separate fields
    parts = cleaned_line.split(",")
    
    parsed_dict = {}
    for part in parts:
        if "=" in part:
            key_val = part.split("=")
        elif ":" in part:
            key_val = part.split(":")
        else:
            continue
            
        if len(key_val) == 2:
            key = key_val[0].strip()
            val = key_val[1].strip()
            
            # Try converting to numeric if possible
            try:
                if "." in val:
                    val = float(val)
                else:
                    val = int(val)
            except ValueError:
                pass  # Keep as string if it cannot be converted
                
            parsed_dict[key] = val
            
    return parsed_dict

def status_of(record_dict):
    """Determines the status based on rating and age."""
    rating = record_dict.get("rating", 0)
    if rating >= 4:
        return "OK"
    else:
        return "FLAGGED"


# ==================== INPUT ====================
# Load raw messy records (at least 5 messy lines)
raw_records = [
    "   Survey_2026 , RATING= 4 , AGE = 23   ",
    "SURVEY_2027, rating=3, age=25",
    "   survey_2028 , RATING=5, AGE=22",
    "survey_2029, rating = 2 , age = 30",
    "   SURVEY_2030, RATING=4, AGE=20   "
]


# ==================== PROCESS + OUTPUT ====================
total_records = 0
flagged_count = 0

for raw_record in raw_records:
    total_records += 1
    parsed_data = parse_line(raw_record)
    current_status = status_of(parsed_data)
    
    if current_status == "FLAGGED":
        flagged_count += 1
        
    print()
    print("=" * 40)
    print(f" Parsed Record : {parsed_data}")
    print(f" Status        : {current_status}")
    print("=" * 40)

print()
print(f"Total records processed: {total_records}")
print(f"Total records flagged: {flagged_count}")

# ==================== 4. Before you finish: ====================
#
# [ ] Run it against at least 5 genuinely messy raw records
# [ ] Run it with a value that will not convert to a number - write the error down
# [ ] Check every function does one job, with a docstring