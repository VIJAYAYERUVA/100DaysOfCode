# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    mylist = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        mylist.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(mylist[:0:-1] + mylist))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
