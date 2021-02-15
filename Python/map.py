# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    mylist = [0, 1]
    for i in range(2, n):
        mylist.append(mylist[i - 2] + mylist[i - 1])
    return (mylist[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
