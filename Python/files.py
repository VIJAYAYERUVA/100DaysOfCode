openfile = open('data/input/read.txt')
a = openfile.read()
print(a)

openfile.seek(0)
b = openfile.read()
print(b)

openfile.seek(0)
for line in open('data/input/read.txt'):
    print(line)

writefile = open('data/output/write.txt', 'r+')
writefile.write('New line in the file')
writefile.seek(0)

c = writefile.read()
print(c)
