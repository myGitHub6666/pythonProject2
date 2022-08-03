filename = "ex26.py"
# filename = input('请输入文件名：')
txt = open(filename, encoding="utf-8")
file = txt.read()
print("<<<\n", file)
#  如何先判断文件是否存在？？不存在可以新建。
newfile = input("请输入用户文件：")
if newfile:
    txt1 = open('newfile.txt', 'w', encoding="utf-8")
else:
    txt1 = open('newfile.txt',"x",encoding="utf-8")
txt1.write(file)
txt.close()
