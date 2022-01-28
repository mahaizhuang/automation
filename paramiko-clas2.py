# /bin/python
import paramiko
import sys
import os 
import time
#
class ssh1(object):
      def __init__(self,host1,username1,password1):
          self.trans = paramiko.Transport((host1, 22))
          self.trans.start_client()
          self.trans.auth_password(username=username1, password=password1)
          self.channel = self.trans.open_session()
          self.channel.settimeout(7200)
          self.channel.get_pty()                                 
          self.channel.invoke_shell()
          print ("登录操作的主机是 %s" %host1)
      def run_list(self,cmdlist):
          f = open(cmdlist, "r",encoding="utf-8")
          for key1 in f:
              self.channel.send(key1)
              time.sleep(2)
              while True:
                  rst = self.channel.recv(1024)
                  rst = rst.decode('utf-8')
                  print(rst)                                         
                  if 'remove' in rst:                                            #linux提示
                      self.channel.send('yes\r')
                      time.sleep(2)
                      ret = self.channel.recv(1024)
                      ret = ret.decode('utf-8')
                      print(ret)
                  break
          f.close()
      def run_cmd(self,cmd1):
          self.channel.send(cmd1)
          time.sleep(1)
          while True:
              rst = self.channel.recv(1024)
              rst = rst.decode('utf-8')
              print(rst)
              if 'remove' in rst:                                                   #linux提示
                  self.channel.send('yes\r')                   
                  time.sleep(1)
                  ret = self.channel.recv(1024)
                  ret = ret.decode('utf-8')
                  print(ret)
              break     
      def run_net(self,netcmdlist):                                                #由配置文件进行无脑定配置
          str1 =""""""
          f = open(netcmdlist, "r",encoding="utf-8")
          for key1 in f:
              self.channel.send(key1)
              time.sleep(1)
              rst = self.channel.recv(1024)
              rst = rst.decode('utf-8')
              print(rst)
              str1 = str1 + "\n" + rst
          f.close()
          return str1
      def close(self):
          #self.channel.send('quit\ %r1' %'\r')
          clscmd=['save','y','','y']
          for key1 in clscmd:
              self.channel.send(key1)
              self.channel.send('\r')
              time.sleep(3)
              ret = self.channel.recv(1024)
              ret = ret.decode('utf-8')
              print(ret)
          self.channel.close()
          self.trans.close()
#
if __name__ == '__main__':
    with open('D:/IT/Hello World/python/网络自动化/ip.txt',"r",encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        host1,username1,password1 = line.strip().split(' ')
        a = ssh1(host1,username1,password1)
        #s = a.run_net('D:/IT/Hello World/python/网络自动化/cmd.txt')
        #with open("D:/IT/Hello World/python/网络自动化/ %s.txt" %host1, "a+",encoding='utf-8') as out_file:
        #     out_file.write(s)
        #     out_file.close()
        a.close()
    f.close()
############################################################################################################
