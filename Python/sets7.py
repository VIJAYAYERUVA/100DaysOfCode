# https://www.hackerrank.com/challenges/py-set-mutations/problem

nA = int(input())
A = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    comm, ne = input().split()
    opSet = set(map(int, input().split()))
    if comm == 'intersection_update':
        A.intersection_update(opSet)
    elif comm == 'update':
        A.update(opSet)
    elif comm == 'difference_update':
        A.difference_update(opSet)
    elif comm == 'symmetric_difference_update':
        A.symmetric_difference_update(opSet)

print(sum(A))
