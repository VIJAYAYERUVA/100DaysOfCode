# Number divisible by 35 between 1500 and 2700
nl = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(nl)
print(','.join(nl))
