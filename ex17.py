from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print(f"ready,hit return to continue,CTRL-c to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright,all done")

out_file.close()
in_file.close()

# 把test.txt拷贝到test1.txt的文件中。
# 打开第一个文件
# 读取文件中的数据，并保存在一个变量中
# 第一个文件的大小是多少字节
# 判断一下第二个文件是否存在。不存在就要新建。拷贝的话相当于是清空之前的文件内容，用w+方式
# 打开新文件
# 把第一个文件获取的数据写入到现有的文件中
# 关闭文件。
