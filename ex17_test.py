from sys import argv
from os.path import exists
script, file1, file2 = argv

print(f"从{file1}拷贝到{file2}")
txt = open(file1)
date = txt.read()
print(f"判断一下{file1}有{len(date)}个字节")
# file.exists()  这样写是错误的，字符串没有这个用法
# exists(file2)结果是布尔型。
print(f"判断一下{file2}是否存在？{exists(file2)}")
input('存在吗？：')
f = open(file2,"w+")
f.write(date)
f.close()
txt.close()

# 格式化字符串太强大了。{相当于直接获取数据}