import subprocess
import time
start_time = time.time()                                   # 记录开始执行的时间
ip_list = ['192.168.124.'+str(i) for i in range(1,255)]    # 定义用来ping的254个ip
#
for ip in ip_list:
    res = subprocess.call('ping -n 2 -w 5 %s' %ip,stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
    print(ip,True if res == 0 else False)
    if res ==0:
        print(ip,file=open('D:/Tool/vscode/微编程/py/network/ip-tru.txt', 'a+'))
    else:
        print(ip,file=open('D:/Tool/vscode/微编程/py/network/ip-li.txt', 'a+'))
#
print('执行所用时间：%s' % (time.time() - start_time),'秒')
#
