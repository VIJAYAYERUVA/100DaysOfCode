# https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    x, A, y, B = input(), set(input().split()), input(), set(input().split())
    print(A.issubset(B))
