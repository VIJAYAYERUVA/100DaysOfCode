# https://www.hackerrank.com/challenges/python-power-mod-power/problem

a, b, m = [int(input()) for _ in '123']
print(pow(a, b), pow(a, b, m), sep='\n')
