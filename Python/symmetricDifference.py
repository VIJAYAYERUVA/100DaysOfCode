# https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
m = input()
m = list(map(int, m.split()))
N = int(input())
n = input()
n = list(map(int, n.split()))

mset = set(m)
nset = set(n)

mun = mset.union(nset)
min = mset.intersection(nset)
mdiffn = mun - min

for i in sorted(mdiffn):
    print(i)
