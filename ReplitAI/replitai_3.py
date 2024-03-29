"""
Canonical Solution:

def compare_one(a, b):
  temp_a, temp_b = a, b
  if isinstance(temp_a, str):
    temp_a = temp_a.replace(',', '.')  # Replace comma with dot in strings
  if isinstance(temp_b, str):
    temp_b = temp_b.replace(',', '.')  # Replace comma with dot in strings
  if float(temp_a) == float(temp_b):
    return None  # Values are equal
  return a if float(temp_a) > float(temp_b) else b  # Return larger value in original type
"""

# Create a Python function compare_one that takes integers, floats, or strings representing real numbers, and returns the larger variable in its given variable type. Return None if the values are equal . Note : If a real number is represented as a string , the floating point might be . or ,
def compare_one(val1, val2):
    if type(val1) in [int, float] and type(val2) in [int, float]:
        return val1 if val1 > val2 else val2 if val2 > val1 else None
    elif isinstance(val1, str) and isinstance(val2, str):
        val1 = val1.replace(",", ".")
        val2 = val2.replace(",", ".")
        return val1 if float(val1) > float(val2) else val2 if float(val2) > float(val1) else None

def check(candidate):
  
  assert candidate(1, 2) == 2
  assert candidate(1, 2.5) == 2.5
  assert candidate(2, 3) == 3
  assert candidate(5, 6) == 6
  assert candidate(1, "2,3") == "2,3"
  assert candidate("5,1", "6") == "6"
  assert candidate("1", "2") == "2"
  assert candidate("1", 1) == None

check(compare_one)

