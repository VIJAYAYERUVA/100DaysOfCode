# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
d = {}
for _ in range(n):
    k = input()
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

print(len(d))

for i in d:
    print(d[i], end=' ')
