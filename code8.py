# 异常处理
try:
    '''
    有可能出现的异常
    '''
    mylist = [1,2,34]
    print(mylist[6])
    pass
except Exception as msg:

    print('异常信息是：',msg)
    '''
    这里是捕获全部异常，出现异常后，打印的异常信息
    '''
    pass
except NameError as msg:
    print(msg)
    pass
else:
    '''
    如果没有出现遗产，执行的代码
    '''
    pass
finally:
    print('执行完毕')