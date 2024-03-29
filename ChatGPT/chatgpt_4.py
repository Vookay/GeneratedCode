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
def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    for i in range(len(s), -1, -1):
        if is_palindrome(s[:i]):
            return s + s[:i][::-1]

"""
def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    if is_palindrome(s):
        return s
    
    for i in range(len(s), -1, -1):
        if is_palindrome(s[:i]):
            return s + s[:i - 1][::-1]
"""

def check(candidate):
  assert candidate('') == ''
  assert candidate('x') == 'x'
  assert candidate('xyz') == 'xyzyx'
  assert candidate('xyx') == 'xyx'
  assert candidate('jerry') == 'jerryrrej'

check(make_palindrome)
