# count the occurrences of a list item
myList = ['Vijaya', 'Yeruva', 'Taj', 'Yeruva']
X = [[x, myList.count(x)] for x in set(myList)]
Y = dict((x, myList.count(x)) for x in set(myList))
print(X)
print(Y)
