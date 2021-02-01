# https://www.hackerrank.com/challenges/py-set-union/problem
n = input()
ns = list(map(int, input().split()))

b = input()
bs = list(map(int, input().split()))

news = set(ns) | set(bs)
print(len(news))
