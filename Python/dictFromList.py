import itertools
import pickle
import re

# Path to the file
filepath = 'data/input/terms.txt'


# definition to convert the data into list
def read_words(path):
    with open(path, 'r') as f:
        return list(itertools.chain.from_iterable(line.split("\n") for line in f))


# definition to save the dictionary
def save_obj(obj, name):
    with open('data/output/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# definition to load the dictionary
def load_obj(name):
    with open('data/output/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# convert the data into list
termsList = read_words(filepath)
filterTermsList = filter(None, termsList)  # filter empty values

onlyLetters = []

for term in filterTermsList:
    onlyLetter = " ".join(re.findall("[a-zA-Z]+", term))
    if onlyLetter:
        onlyLetters.append(onlyLetter)
onlyLetters = sorted(onlyLetters)

# length of final list
num_lines = len(onlyLetters)

# creating the dictionary from list
termsDictionary = {key: value for (key, value) in zip(range(num_lines), onlyLetters)}

# save the dictionary
save_obj(termsDictionary, 'termsDictionary')

# load the dictionary
finalDictionary = load_obj('termsDictionary')

print(finalDictionary)
