"""
Desc:
Using str.find(str, start, end) to find substring in sliced string
"""

in_str = 'The most popular Python versions are Python 2.6, and Python 3.6.'
find_str = 'Python'

start = in_str.find(find_str) + len(find_str)
end = len(in_str)

ret_index = in_str.find(find_str, start, end)

print(f"The input string is: {in_str}")
print(f"The position of '{find_str}' in sliced string '{in_str[start:end]}' is: {ret_index}")
