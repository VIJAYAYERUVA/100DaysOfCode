# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    commands = []
    for _ in range(N):
        c = input()
        commands.append(c)
    output = []
    for c in commands:
        if c.split()[0] == 'insert':
            output.insert(int(c.split()[1]), int(c.split()[2]))
        elif c.split()[0] == 'remove':
            output.remove(int(c.split()[1]))
        elif c.split()[0] == 'append':
            output.append(int(c.split()[1]))
        elif c.split()[0] == 'sort':
            output = output.sort()
        elif c.split()[0] == 'pop':
            output.pop()
        elif c.split()[0] == 'reverse':
            output.reverse()
        elif c.split()[0] == 'print':
            print(output)
        else:
            pass
