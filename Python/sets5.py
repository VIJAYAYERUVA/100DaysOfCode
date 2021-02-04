# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
nStudents = set(map(int, input().split()))
b = int(input())
bStudents = set(map(int, input().split()))

print(len(nStudents - bStudents))
