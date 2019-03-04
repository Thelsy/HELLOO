#!/Users/lsy python
# coding:utf-8
# lsy
import paramiko
import logging
import sys
import time
'''定义操作命令类'''
class Shell():
    def __init__(self, hostname, port, username, password):
        # 初始化属性
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
    def servcer(self,cmd):
        '''连接操作服务器'''
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.hostname, self.port, self.username, self.password, compress=True, timeout=5)
            time.sleep(3)
            print(self.hostname+'&'+'连接成功')
            while True:
                print(cmd)
                stdin, stdout, stderr = client.exec_command(cmd)
                # stdin.write('Y')
                out = stdout.read()
                if not out:
                    out = stderr.read()
                client.close()
                stt = out.decode()
                return stt
        except Exception as e:
            print('连接失败请检查账号密码:'+'&'+str(e))
    def logout(self,cmd):
        if 'exit' in cmd:
            logging.warning('退出')
            time.sleep(1)
            sys.exit()
    def warning(self,cmd):
        if 'rm -rf ' in cmd:
            logging.warning('警告删除操作!请检查命令')
            print(cmd)
            s = input('请确认是否删除(y/n)')
            if s == 'y':
                time.sleep(1)
            else:
                logging.warning('退出')
                sys.exit()




