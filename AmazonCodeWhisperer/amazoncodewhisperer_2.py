"""
Canonical Solution:

def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False  # Empty dictionary
    state = "start"
    for key in dict.keys():
        if not isinstance(key, str):
            state = "mixed"
            break
        if state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                break  # Key is neither uppercase nor lowercase
        elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
            state = "mixed"
            break
    return state == "upper" or state == "lower"
"""

# Create a Python function check_dict_case for the following problem: Given a dictionary, return True if all keys are strings in lower case or all keys are strings in upper case, else return False. The function should return False is the given dictionary is empty.

def check_dict_case(dict1):
  if not dict1:
    return False

  key_case = None
  
  for key in dict1:
    if key_case is None:
      key_case = key.islower() or key.isupper()
    else:  
      if (key.islower() and not key_case) or (key.isupper() and not key_case):
        return False

  return True

"""
Fix (incorrect):
import typing

def check_dict_case(dict1: typing.Dict[str, typing.Any]) -> bool:

  if not dict1:
    return False

  key_case = None

  for key in dict1:
    
    if not isinstance(key, str):
      raise TypeError("Dictionary keys must be strings")
      
    key_lower = key.lower()
    
    if key_case is None:  
      key_case = key_lower == key or key_upper == key
    else:
      if (key_lower == key and key_case != key_lower == key) or \
         (key_upper == key and key_case != key_upper == key):
        return False

  return True
"""

def check(candidate):

  assert candidate({"p": "pineapple", "b": "banana"}) == True, "First test error: " + str(candidate({"p": "pineapple", "b": "banana"}))
  assert candidate({"p": "pineapple", "A": "banana", "B": "banana"}) == False, "Second test error: " + str(candidate({"p": "pineapple", "A": "banana", "B": "banana"}))
  assert candidate({"p": "pineapple", 5: "banana", "a": "apple"}) == False, "Third test error: " + str(candidate({"p": "pineapple", 5: "banana", "a": "apple"}))
  assert candidate({"Name": "John", "Age": "36", "City": "Houston"}) == False, "Fourth test error: " + str(candidate({"Name": "John", "Age": "36", "City": "Houston"}))
  assert candidate({"STATE": "NC", "ZIP": "12345"}) == True, "Fifth test error: " + str(candidate({"STATE": "NC", "ZIP": "12345"}))
  assert candidate({"fruit": "Orange", "taste": "Sweet"}) == True, "Sixth test error: " + str(candidate({"fruit": "Orange", "taste": "Sweet"}))

  assert candidate({}) == False, "1st edge test error: " + str(candidate({}))

check(check_dict_case)