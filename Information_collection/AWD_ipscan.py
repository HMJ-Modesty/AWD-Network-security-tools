# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : AWD_ipscan.py
# 时间    : 2022/9/28 20:39
# -----------------------------------------------------------------------------------

# 导入 requests 包
from matplotlib.pyplot import switch_backend
import requests
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 写入ip
file = open('../Information_collection/iplist.txt', "w")
for i in range(256):
    ip = "http://192-168-1-" + str(i) + ".awd.bugku.cn"
    # ip = "http://192-168-1-" + str(i) +".pvp1522.bugku.cn"
    # ip = "http://192.168.56." + str(i)+"/awd"
    file.write('{}\n'.format(ip))
file.close()

# 读取ip
iplist = []
file = open("../Information_collection/iplist.txt", "r")
for f in file:
    ip_list = f.strip()
    iplist.append(ip_list)
file.close()


def scan(x, y):
    s = requests.Session()
    file = open('../Information_collection/ip_result_of_scanning.txt', "a+")
    for i in range(x, y):
        try:
            # 发送请求
            print("正在扫描目标请耐心等待.... ...." + iplist[i])
            response = s.get(iplist[i], headers=headers, timeout=1)
            # response = requests.get(iplist[i],headers = headers,timeout=1)
            code = response.status_code
            if code == 200:
                print(iplist[i])
                file.write('{}\n'.format(iplist[i]))
            else:
                pass
        except requests.exceptions.RequestException as e:
            pass
    file.close()


def Threads(amount, total):
    for i in range(amount):
        y = (total / amount)
        x = i * (total / amount)
        thread = threading.Thread(name='i', target=scan, args=(int(x), int(x + y)))
        thread.start()  # 启动线程


if __name__ == "__main__":
    print("开始扫描")
    Threads(256, 256)
