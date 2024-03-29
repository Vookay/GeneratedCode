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
def check_dict_case(my_dict):
  if not my_dict:
    return False
  
  all_lower = all(key.islower() for key in my_dict.keys())
  all_upper = all(key.isupper() for key in my_dict.keys())

  return all_lower or all_upper

"""
def check_dict_case(my_dict):
  if not my_dict:
    return False
  all_strings = all(isinstance(key, str) for key in my_dict.keys())
  if all_strings:
    all_lower = all(key.islower() for key in my_dict.keys())
    all_upper = all(key.isupper() for key in my_dict.keys())
    return all_lower or all_upper
  else:
    return False
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