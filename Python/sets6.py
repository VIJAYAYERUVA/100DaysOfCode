# https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
nStudents = set(map(int, input().split()))
b = int(input())
bStudents = set(map(int, input().split()))

a = nStudents.symmetric_difference(bStudents)

for i in sorted(a):
    print(i)
