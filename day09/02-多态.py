# pyhton本质上是没有多态的（约定俗成）
# 多台：关心的是同一个方法，但是会出现不同形式

class Text(object):
    def show(self):
        print("显示文字")


class Image(object):
    def show(self):
        print("显示图片")


class Video(object):
    def show(self):
        print("显示音频")


# 显示数据的方法
def show_data(data):
    # 关心的是同一个方法：会有不同表现形式
    # 在python里面的多态只关心对象的方法，不关心对象的类型
    data.show()


t = Text()
i = Image()
v = Video()

show_data(v)
