from sys import argv

script, filename = argv

print(f"we're going to earse {filename}.")
print("If you don't want that,hit CTRL_C (c).")
print("if you do want that,hit RETZURN.")

input("?")

print("opening the file...")
# w是只写模式打开文件
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# 从此处进行文件截取。后面的部分区全部删除。应该是全部都删除了。
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")
# 优化底下6行代码
target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally,we close it. ")
target.close()

