# 导入 requests 包
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 写入ip
file = open('iplist.txt', "w")
for i in range(255):
    #ip = "https://192-168-1-" + str(i) +".awd.bugku.cn"
    ip = "http://39.156.66." + str(i)
    file.write('{}\n'.format(ip))
file.close()

# 读取ip
iplist = []
file = open("iplist.txt", "r")
for f in file:
    ip_list = f.strip()
    iplist.append(ip_list)
file.close()

file = open('ip_result_of_scanning.txt', "w")
for url in iplist:
    try:
# 发送请求
        response = requests.post(url,headers = headers,timeout=1)
# response = requests.post(url)
        code = response.status_code
        if  code == 200:
            print(url)
            file.write('{}\n'.format(url))
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass
file.close()