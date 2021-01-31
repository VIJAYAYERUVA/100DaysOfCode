# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
from typing import Set

n = int(input())
s: Set[int] = set(map(int, input().split()))
N = int(input())

for i in range(N):
    choice = input().split()
    if choice[0] == "pop":
        s.pop()
    elif choice[0] == "remove":
        s.remove(int(choice[1]))
    elif choice[0] == "discard":
        s.discard(int(choice[1]))
print(sum(s))
