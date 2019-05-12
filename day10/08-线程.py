# 线程：执行代码的分支，默认只有一个线程，（主线程）
# python本质没有多线程（假象）
import threading
import time


def AA(count):
    for i in range(count):
        print("aa")
        time.sleep(1)


def BB(count):
    for i in range(count):
        print("bb")


if __name__ == '__main__':
    sub_thread = threading.Thread(target=AA, args=(10,))
    # 启动线程（执行子线程的操作）
    sub_thread.start()
    # 在主线程调用函数
    three_thread = threading.Thread(target=BB, kwargs={"count": 5})
    three_thread.start()
# 线程是无序的
