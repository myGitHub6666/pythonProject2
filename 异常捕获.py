# try:
#     书写可能发生的异常代码
# except： 任何类型的异常都可以捕获
#     发生了异常要执行的代码
# try:
#     书写可能发生的异的代码
# except 异常德类型：只能捕获指定的异常，如果不是这个类型的异常，还是还会报错
#     发生了异常仍然药品执行的代码
# try:
#     num = input("请输入数字：")
#     num = int(num)
#     print(num)
# except ValueError: # 只能捕获Valueerror类型及其子类的异常
#     print("请输入正确的数字")
# # 捕获多个指定异常
# try:
#     书写 可能发生异常德代码
# except 异常类型1：
#     发生异常类型1后执行的代码，只能捕获特定异常，如果不是这个异常，还是会报错
# except 异常类型2：
#     发生异常类型2执行的代码
# try:
#     num = input("请输入数字")
#     num = int(num)
#     a = 10/num
#     print(f"a={a}")
# except ValueError:
#     print("发生了异常，请输入正确的数字，不要输入字符")
# except ZeroDivisionError:
#     print("请不要输入0")
# print("结束")
# 异常捕获的完整版本
# try:
#     可能发生异的代码
# except Exception as 变量: exception是常见异常的父类，可以捕获常见的所有异常。变量的话，是异常类的一个对象，可以把异常信息打印出来
#     发生其他类型的异常执行的代码
# else：
#     没有发生异常会执行的代码
# finally：
#     不管有没有发生异常都会执行的代码
try:
    num = input("请输入数字")
    num = int(num)
    a = 10 / num
    print(f'a={a}')
except Exception as e:
    print(f"错误信息为{e}")
else:
    print("没有发生异常我会执行")
finally:
    print("不管有没有发生异常我都会执行")
    






