"""
 Desc:
  Using find() when the string has two or more occurrences of a substring
"""

in_str = 'The most popular Python versions are Python 2.6, and Python 3.6.'
find_str = 'Python'

ret_index = in_str.find(find_str)

print(f"The input string is: {in_str}")
print(f"The position of '{find_str}' substring is: {ret_index}")
