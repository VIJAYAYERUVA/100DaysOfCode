def wrap(string, max_width):
    s = ''
    for word in range(0, len(string), max_width):
        s += string[word:word + max_width] + "\n"
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
