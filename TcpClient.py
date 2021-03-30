# !/usr/bin/python3
import threading
import time
import socket
import sys

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("myThread 开始线程：" + self.name)

class SocketHelper(myThread):
    def __init__(self):
        myThread.__init__(self)
        self.stop = False

    def socketStart(self):
        self.connect()

    def connect(self):
        try:
            # 尝试连接服务端
            self.sock.connect(self.address)
            self.recvMsg()
        except Exception:
            print('[!] Server not found ot not open')
            sys.exit()

    def stop(self):
        self.sock.close()

    def sendMsg(self):
        trigger = input('Input: ')
        self.sock.sendall(trigger.encode())

    def recvMsg(self):
        while not self.stop:
            data = self.sock.recv(1024)
            data = data.decode()
            print('[Recieved]', data)

    def run(self):
        print("SocketHelper 开始线程：" + self.name)
        # 服务端地址和端口
        ip = socket.gethostbyname("www.wuweidong.site")
        self.address = (ip,9000)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketStart()





