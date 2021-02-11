# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(input().split())
counter, n = 0, int(input())
for i in range(n):
    B = set(input().split())
    if A.issuperset(B):
        counter += 1
print(counter == n)
