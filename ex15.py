# 导包
# from sys import argv
# # 外部获取filename的值。script的值是ex15文件本身
# script, filename = argv
# # 加载或者打开filename这个文件。txt是一个文件对象，并不是文件本身
# txt = open(filename)
filename = input(">")
txt = open(filename, "w+")
# 打印
print(f"Here's your file {filename} :")
# 把文件读取出来并打印出来
print(txt.read())
print(txt.write("nihao"))
txt.close()
# 打印
print("Type thew filename again:")
# 从键盘输入文件的名字
file_again = input(">")
# 打开file——again这个文件
txt_again = open(file_again)
# 读取file——again这个文件并打印
print(txt_again.read())
