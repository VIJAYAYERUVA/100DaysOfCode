import string

alphabets = set(string.ascii_lowercase)
print('Alphabets: ', sorted(alphabets))

input_strings = ['We promptly judged antique ivory buckles for the next prize',
                 'string not contains every letter of the alphabet']

for input_string in input_strings:
    if set(input_string.lower()) >= alphabets:
        print('Input string: ', input_string)
        print('Letters in the input: ', sorted(set(input_string.lower())))
        print('The above string contains all letters of the alphabets')
    else:
        print('Input string: ', input_string)
        print('Letters in the input: ', sorted(set(input_string.lower())))
        print('The above string does not contain all letters of the alphabets')
