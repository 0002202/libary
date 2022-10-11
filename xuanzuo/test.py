import threading
import time

# 签到模块
def login_in():
    # 用户手动签到
    print("进行签到")
    return 1

# 签到成功后执行
def success():
    print('签到成功')

# 超时签到
def leave():
    # 超时处理
    print("签到失败")

# 一直执行签到计时，多线程
def sleep():
    global lock, n
    lock.acquire()  
    print('开始计时')
    time.sleep(2)
    # if n is not None:
    #     time.sleep(2)
    leave()
    lock.release()

# 判断计时，多线程
def job():
    global lock, n
    # n = None
    lock.acquire()    # 锁住线程
    # 判断用户是否完成签到
    if n is not None:
        # 签到成功
        success()
    else:
        # 超时处理
        print("超时处理")
        sleep()
        print("继续计时")        
    lock.release()

def main():
    added = threading.Thread(target=job, name='判断签到')     # 创建线程，target定义功能不能带括号，只是一个索引,name命名线程，参数使用arags进行传参
    sleep1 = threading.Thread(target=sleep, name='睡眠')
    sleep1.start()             # 运行指令
    added.start()              # start的时间取决于线程的开始时间
    # added.join()               # join后面的需要线程结束后进行运行
    sleep1.join()


if __name__=='__main__':
    print('准备签到')
    lock = threading.Lock()
    # n = login_in()
    n = None
    main()
    