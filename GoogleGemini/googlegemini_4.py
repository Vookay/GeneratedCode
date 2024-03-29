"""
Canonical Solution:

def is_palindrome(string: str) -> bool:
  return string == string[::-1]

def make_palindrome(string: str) -> str:
  if not string:
    return ''  # Empty string is a palindrome

  beginning_of_suffix = 0

  # Find the longest postfix of the string that's a palindrome
  while not is_palindrome(string[beginning_of_suffix:]):
    beginning_of_suffix += 1

  # Append the reverse of the prefix that's not a palindrome to the original string
  return string + string[:beginning_of_suffix][::-1]

"""

# Create two Python functions: is_palindrome, that tests if given string is a palindrome, and make_palindrome, that finds the shortest palindrome that begins with a supplied string, the algorithm consists of finding the longest postfix of supplied string that is a palindrome and appending to the end of the string reverse of a string prefix that comes before the palindromic suffix.
def is_palindrome(text):
  text = ''.join(char.lower() for char in text if char.isalnum())
  return text == text[::-1]

def make_palindrome(text):
  longest_suffix = ""
  for i in range(len(text), 0, -1):
    suffix = text[-i:]
    if is_palindrome(suffix):
      longest_suffix = suffix
      break

  prefix = text[:-len(longest_suffix)]
  return text + prefix[::-1]

def check(candidate):
  assert candidate('') == ''
  assert candidate('x') == 'x'
  assert candidate('xyz') == 'xyzyx'
  assert candidate('xyx') == 'xyx'
  assert candidate('jerry') == 'jerryrrej'

check(make_palindrome)
