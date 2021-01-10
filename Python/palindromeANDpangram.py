def palindrome(s):
    s = ''.join(filter(str.isalpha, s))
    rs = s[::-1]
    return s == rs


def ispangram(str1):
    str1 = ''.join(filter(str.isalpha, str1))
    str1 = set(str1.lower())
    return len(str1) == 26


pal = 'nurses run'
pan = 'The quick brown fox jumps over the lazy dog'
if palindrome(pal):
    print(f'"{pal}" is a palindrome')

if ispangram(pan):
    print(f'"{pan}" is a pangram')
