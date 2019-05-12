# 子线程和主线程会产生资源竞争
# 创建互斥锁：保证同一时刻，只能一个线程去执行代码
# 这样全局变量不会存在资源竞争的问题
import threading

lock = threading.Lock()
g_num = 0


def AA():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(10000000):
        g_num += 1
    # 释放锁
    lock.release()
    print("AA", g_num)


def BB():
    lock.acquire()
    global g_num
    for i in range(10000000):
        g_num += 1
    lock.release()
    print("BB", g_num)


if __name__ == '__main__':
    # 创建两个线程
    first = threading.Thread(target=AA)
    second = threading.Thread(target=BB)
    first.start()
    second.start()
