#!/Users/lsy python
# coding:utf-8
# lsy
from toolrstart.shell import Shell
import time

class Codeif():
    def codeif(self):
        ip = input('请输入要连接的ip地址:')
        port = input('请输入端口号，默认22端口：')
        username = input('请输入要登录的用户名：')
        password = input('请输入密码:')
        if port == '':
            port = 22
        cmd = 'ps -ef |grep java'
        ssh = Shell(ip, port, username, password)
        dos = ssh.servcer(cmd)
        print(dos)
        while True:
            if '/data/workspace/bin' in dos:
                time.sleep(3)
                i = input('检查到启动脚本在/data目录下是否重启(y/n):')

                if i == 'y':
                    cmd = 'sh /data/workspace/bin/server.sh restart all'
                    ssh.logout(cmd)
                    ssh.warning(cmd)
                    dos = ssh.servcer(cmd)
                    print(dos)

                else:
                    cmd = input('请输入要执行的命令(多条命令以;分隔):')
                    ssh.logout(cmd)
                    ssh.warning(cmd)
                    dos = ssh.servcer(cmd)
                    print(dos)

            else:
                cmd = input('请输入要执行的命令(多条命令以;分隔):')
                ssh.logout(cmd)
                ssh.warning(cmd)
                dos = ssh.servcer(cmd)
                print(dos)


