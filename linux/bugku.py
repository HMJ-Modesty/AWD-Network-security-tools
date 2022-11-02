# -*- coding: utf-8 -*-
# 作者    : 轩昂妄想
# 文件    : bugku.py
# 时间    : 2022/10/27 21:00
# -----------------------------------------------------------------------------------
import requests
import urllib3
import re

urllib3.disable_warnings()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}


def checkin(s, bugkucookie):
    bugkucookie = bugkucookie.strip()
    global headers
    headers['cookie'] = bugkucookie
    s.get("https://ctf.bugku.com/", headers=headers, verify=False, timeout=40)
    info = s.get("https://ctf.bugku.com/user/checkin", headers=headers, verify=False, timeout=40).text.split(
        '<h3 class="m-t-30">')[1].split('</')[0]
    tip(info.strip())


def tip(text):
    data = {'desp': text}
    # 你的server酱 key 用来发送微信通知
    your_ftqq_key = 'SCUxxxx'
    requests.post("https://sc.ftqq.com/" + your_ftqq_key + ".send?text=BUGKU自动签到", data=data)


def main():
    s = requests.Session()
    global headers
    githubloginurl = "https://github.com" + \
                     s.get("https://ctf.bugku.com/login", headers=headers, verify=False, timeout=40).text.split(
                         'https://github.com')[1].rsplit('"')[0]
    # 填写你的github cookie 理论只需以下两段就行，并且以下两段的值是相同的。
    githubcookie = "user_session=JEv4eQSEfho-Wu4vYUiJfkjBlgenydJ2FMCC0Xqwflm9M9Fk; __Host-user_session_same_site=JEv4eQSEfho-Wu4vYUiJfkjBlgenydJ2FMCC0Xqwflm9M9Fk;"
    headers['cookie'] = githubcookie
    if (s.get("https://github.com/settings/profile", headers=headers, verify=False, timeout=40,
              allow_redirects=False).status_code != 200):
        tip("github Cookie 失效")
    res = s.get(githubloginurl, headers=headers, verify=False, timeout=40)
    if ("登录成功" in res.text):
        print("成功获取到Cookie")
        for bugkucookie in res.headers['Set-Cookie'].split(','):
            # print(bugkucookie)
            if ('PHPSESSID' in bugkucookie):
                checkin(s, bugkucookie)
                break
    elif ("github.githubassets.com" in res.text):
        print("github 二次点击校验")
        form = res.text.split('<form action="')[1].split('<input type="hidden" name="scope"')[0]
        p = re.compile('name="(.*?)".*?value="(.*?)"')
        formdata = p.findall(form)
        data1 = {}
        for x in formdata:
            data1[x[0]] = x[1]
        data1['authorize'] = 1
        formurl = "https://github.com" + form.split('"')[0]
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "cookie": githubcookie
        }

        res = s.post(formurl, data=data1, headers=headers, verify=False, timeout=40)
        if ("登录成功" in res.text):
            print("成功获取到Cookie")
            for bugkucookie in res.headers['Set-Cookie'].split(','):
                print(bugkucookie)
                if ('PHPSESSID' in bugkucookie):
                    checkin(s, bugkucookie)
                    print("签到成功！！！")
                    break
        else:
            tip("fail")
    else:
        tip("fail")


print("开始！！！")
main()
