# class Login:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

def login(username, password):
    if username == 'admin' and password == '123456':
        return '登录成功'
    else:
        return '登录失败'



