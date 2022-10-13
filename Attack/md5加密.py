# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : md5加密.py
# 时间    : 2022/10/13 21:02
# -----------------------------------------------------------------------------------
# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作
import hashlib

# 待加密信息
str = 'busi'
# 创建md5对象
hl = hashlib.md5()
#更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
#md5_obj=hashlib.md5("123456".encode("utf-8")) 效果一样
hl.update(str.encode("utf-8"))
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())