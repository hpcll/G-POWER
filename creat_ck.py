import paramiko
import re

path_file = [5,6,7]

ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
# 这里写我们的密钥文件
# private_key = paramiko.RSAKey.from_private_key_file("key.poem")
# 连接服务器，这里我们用pkey参数设置为私钥登陆
ssh.connect(hostname="47.242.147.185" , port=22 , username="root" , password="Hpc19970122")

def exec_shell(ml):
    stdin , stdout , stderr = ssh.exec_command(ml,get_pty=True)# 执行命令
    msg = stdout.read().decode('utf-8')# 以utf-8编码对结果进行解码
    return msg

if __name__ == '__main__':

    for path in path_file:
        command = ("cd /hupc" + ";" + "mkdir {}" + ";" + "cd {}" + ";" + "mkdir chenggong" + ";" + "pwd").format(path,path)
        print("invoke command ",command)
        msg = exec_shell(command)
        list = msg.split()
        if len(list) == 1:
            print("当前目录为{}".format(list[0]))
        else:
            continue
        print(list)
        ssh.close()
