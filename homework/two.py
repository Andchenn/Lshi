# 实现用户输入用户名和密码，当用户名为seven且密码为123时，显示登录成功，否则登录失败，失败是允许重复输入三次

count = 0

while count < 3:
    username = input('请输入用户名：')
    password = int(input('请输入用户密码：'))
    if username == 'seven' and password == 123:
        print('%s登录成功' % username)
        break
    else:
        print('登录失败')
    count += 1


