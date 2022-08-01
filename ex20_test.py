from sys import argv
script, filename = argv


def print_all(f):
    print(f.read())


def print_0(f):
    f.seek(0)


def print_line(line_count, f):
    print(line_count, f.readline())


print(f"this is {filename} file")
print_all(filename)

print_0(filename)
print("this is a file:")
line_count_ = 1
print_line(line_count_, filename)
line_count_ += 1
print_line(line_count_, filename)
line_count_ += 1
print_line(line_count_, filename)

