# 类（class）：告诉python创建新类型的东西
# 对象（object）：最基本的东西或者某样东西的实例
# 实例（instance）：这就是让python创建的一个类得到的东西
# def ； 这是在类里面定义函数的方法
# self： 在类的函数中，self指被访问的对象或者实例的一个变量
# 继承：指一个类可以继承另一个类的特性，和父子关系类似
# 组合: 指一个类可以将别的类作为他的部件构建起来，有点类似于车子和轮子的关系
# 属性： 类的属性，它来自于组合，而且通常是一个变量
# 是什么（is a）： 用来，描述继承关系
# 有什么（has a） ： 用来描述某个东西是由另外的一些东西组成的，或者某个东西有某些特征

# 创建一个叫X的类，他是Y的一种
# class X(Y):
#     pass
#
# # 类X有一个__init__，它接收self，和J作为参数
# class X(object):
#     def __init__(self,J):
#
# # 类X有一个名为M的函数，它接收self和J作为参数
# class X(object):
#     def M(self,j):
#
# # 将foo设为类X的一个实例
# foo = X()
# # 从foo中找到M函数，并使用self和J作为参数
# foo.M(J)
# # 从foo中获取K属性并将其设置为Q
# foo.k = Q


