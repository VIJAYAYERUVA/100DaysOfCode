# https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s = input().split()
r = 0
if s[1]:
    r = int(s[1])
else:
    r = len(s[0])

per = list(permutations(s[0], r))
per1 = []
for i in per:
    ss = ''.join(list(i))
    per1.append(ss)
for i in sorted(per1):
    print(i)
