def myfunc(mystring):
    s = ''
    for i, l in enumerate(mystring):
        if i % 2 == 0:
            s = s + l.upper()
        else:
            s = s + l
    return s


print(myfunc('vijaya'))
