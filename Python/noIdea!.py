# https://www.hackerrank.com/challenges/no-idea/problem

n, m = input().split()
narray = input().split()
A = set(input().split())
B = set(input().split())

h = 0
s = 0

for i in narray:
    if i in A:
        h = h + 1
    if i in B:
        s = s + 1
print(h - s)
