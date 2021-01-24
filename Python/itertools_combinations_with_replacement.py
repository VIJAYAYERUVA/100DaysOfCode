# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

s = input().split()
r = 0
if s[1]:
    r = int(s[1])
else:
    r = len(s[0])

allcomb = list(combinations_with_replacement(sorted(s[0]), r))

comb = []
for i in allcomb:
    ss = ''.join(list(i))
    comb.append(ss)
sortedcomb = sorted(sorted(comb), key=len)
for i in sortedcomb:
    print(i)
