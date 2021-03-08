# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re


def fun(s):
    # return True if s is a valid email, else return False
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
    return pattern.match(s)


def filter_mail(newemails):
    return list(filter(fun, newemails))


if __name__ == '__main__':
    n = int(input())
    myemails = []
    for _ in range(n):
        myemails.append(input())

    filtered_emails = filter_mail(myemails)
    filtered_emails.sort()
    print(filtered_emails)
