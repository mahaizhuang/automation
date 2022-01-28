import threading
import subprocess
import time
from queue import Queue
WORD_THREAD = 50                            # 定义工作线程
IP_QUEUE = Queue()                          # 将需要 ping 的 ip 加入队列
for i in range(1,255):
    IP_QUEUE.put('192.168.124.'+str(i))
#
def ping_ip():                              # 定义一个执行 ping 的函数
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        res = subprocess.call('ping -n 2 -w 5 %s' % ip,stdout=subprocess.PIPE)
        print(ip,True if res == 0 else False)
#
if __name__ == '__main__':
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_ip)
        thread.start()
        threads.append(thread)
    #
    for thread in threads:
        thread.join()
#
    print('程序运行耗时：%s' % (time.time() - start_time),'秒')
#
