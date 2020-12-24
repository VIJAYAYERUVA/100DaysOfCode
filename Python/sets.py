# Convert Set to String
# https://www.geeksforgeeks.org/convert-set-to-string-in-python/

# Method 1: Using str()

# create a set
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

# convert Set to String
s = str(s)
print("\nAfter the conversion")
print("The datatype of s : " + str(type(s)))
print("Contents of s : " + s)

# Method 2: Using Join()

# create a set
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

# convert Set to String
S = ', '.join(s)
print("The datatype of s : " + str(type(S)))
print("Contents of s : ", S)
