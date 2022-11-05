import requests
from lxml import etree
from requests.packages import urllib3
urllib3.disable_warnings()
 
url = "https://ctf.bugku.com/login"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
 
# 1.创建session对象
session = requests.session()
pag_text = session.get(url=url,headers=headers).text
 
# 2.实例化一个etree对象，方便后面对页面进行数据解析
tree = etree.HTML(pag_text)
 
# 3.提取验证码下载地址
img_path = "https://ctf.bugku.com/" + "https://ctf.bugku.com/captcha.html0.8157776492493183"
 
# 4.下载验证码,以二进制的方式进行保存
img_content = session.get(img_path,headers=headers,verify=False).content
with open('./img.png','wb') as f:
    f.write(img_content)
    print('验证码图片下载成功')
 
# img_code= input('请输入验证码：')
#
# # 5.进行登录，定义post的参数
# data = {
#     'username': 'test123',
#     'password': 'admin@123',
#     'checkcode': img_code,
#     'usecookie': '315360000',
#     'action': 'login',
#     'submit': '立即登陆'
# }
# # 判断是否登录成功
# response = session.post(url=url,data=data,headers=headers,verify=False)
# response.encoding = 'gbk'      #编码防止乱码
# response_text = response.text
# if "登录成功"  in response_text:
#     print("登陆成功")
# # 请求个人信息页
# # ge = session.get(url='https://www.qb5.tw/userdetail.php',headers=headers,verify=False)
# # with open('xs.html','w',encoding='gbk') as f:
# #     f.write(ge.text)
