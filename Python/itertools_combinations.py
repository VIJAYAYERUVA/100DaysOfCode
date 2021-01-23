# https://www.hackerrank.com/challenges/itertools-combinations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s = input().split()
r = 0
if s[1]:
    r = int(s[1])
else:
    r = len(s[0])

allcomb = []
for i in range(1, r + 1):
    comb = list(combinations(sorted(s[0]), i))
    allcomb.extend(comb)

comb = []
for i in allcomb:
    ss = ''.join(list(i))
    comb.append(ss)
sortedcomb = sorted(sorted(comb), key=len)
for i in sortedcomb:
    print(i)
