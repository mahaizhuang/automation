# /bin/python
import paramiko
import sys
import os 
import time
import logging
#
class ssh1(object):
      def __init__(self,host1,username1,password1):
          self.ssh = paramiko.SSHClient()
          self.ssh.load_system_host_keys()
          self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          transport1 = paramiko.Transport((host1, 22))
          transport1.connect(username=username1, password=password1)
          self.ssh._transport = transport1
          print ("登录操作的主机是 %s" %host1)
      def run_cmd(self,cmd):
          stdin, stdout, stderr = self.ssh.exec_command(cmd)
          time.sleep(1)
          res = stdout.read().decode('utf-8')
          return res
      def run_cmdlist(self,cmdlist):
          f = open(cmdlist, "r",encoding="utf-8")
          str1 = """"""
          for key1 in f:
              print (key1)
              stdin, stdout, stderr = self.ssh.exec_command(key1)
              res=stdout.read().decode('utf-8')
              print (res)
              #str1=str1 + "\n" + res
              time.sleep(1)
          f.close()
          return str1
      def close(self):
          self.ssh.close()
#
if __name__ == '__main__':
    #host = ssh1 ("172.30.45.48","admin","Apstackadm&88")
    #host.run_cmdlist("D:/IT/Hello World/python/网络自动化/cmd.txt")
    #host.close()
    with open('D:/IT/Hello World/python/网络自动化/ip.txt',"r",encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        host1,username1,password1 = line.strip().split(' ')
        a = ssh1(host1,username1,password1)
        a1 = a.run_cmd("display current-configuration")
        #a.run_cmdlist()
        print (a1)
        time1 = time.strftime("%Y年%m月%d日", time.localtime());host1l = host1+time1+".txt"
        with open("D:/IT/Hello World/python/网络自动化/ %s" % host1l, "a+",encoding='utf-8') as out_file:
            out_file.write(a1)
            out_file.close()
        a.close()
    f.close()
#
