from sys import argv
script,filename = argv
f = open(filename)
print(f"this is the {filename}:")
print(f.read())
f.close()
filename = input('>')
print(f"please read this file {filename}:")
file = open(filename)
print(file.read())
file.close()
