# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here

    s = sum(set(array)) / len(set(array))
    return s


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
