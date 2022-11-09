# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : 123.py.py
# 时间    : 2022/11/5 19:49
# -----------------------------------------------------------------------------------
import requests

url = "http://192-168-1-211.awd.bugku.cn/waf.php"
while(1):
    requests.get(url)
    print("ok")