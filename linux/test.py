import requests
import urllib3
import ddddocr


def ddddorc_deal(img):
    orc = ddddocr.DdddOcr()
    with open(img, 'rb+') as fp:
        img_bytes = fp.read()
    res = orc.classification(img_bytes)
    return res



urllib3.disable_warnings()

headers1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie": "Hm_lvt_97426e6b69219bfb34f8a3a1058dc596=1667379873,1667394440,1667396393,1667461689; think_lang=zh-cn; PHPSESSID=39e4833e15729ca3684ad8047478f1d5; autoLogin=k9kO6NcQ13o2hQQsxG98rnS9Z0dSe7yDRq2JSwqMjN4RCuAQkGMdGTGaWMD8%2B3gx5kq7vHH6Ov%2BSm5FeMLqI2bhsHlNJEnv%2BAAFPA68gkkgEZCJ8rNMb1BfiNg2WsgXqUgludbEVzG2n; X-CSRF-TOKEN=d86ce30dd470abf39d2f4e8e55933ae9; Hm_lpvt_97426e6b69219bfb34f8a3a1058dc596=1667461689"
}

headers2 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie": "think_lang=zh-cn; PHPSESSID=62c68db8133fb8f247da1514a5fa14e6; autoLogin=xI1Q74QR23k2hQQsxG98rnS9Z0dSe7yDRq2JSwqMjN4RCuAQkGMdGTGaWMD8+3gx40G9vnGta6KSnZUKa+GP2LpjTlMcH3r+VgAeWvglk0sEZCJ8rNMb1BfiNg2WsgXqUgludbEVzG2n; X-CSRF-TOKEN=6aeff5742287362927aaf81adc408684"
}


def checkin(headers):
    a = requests.get("https://ctf.bugku.com/", headers=headers, verify=False, timeout=40)
    info = requests.get("https://ctf.bugku.com/user/checkin", headers=headers, verify=False, timeout=40).text.split(
        '<h3 class="m-t-30">')[1].split('</')[0]
    print(info.strip())


checkin(headers1)
checkin(headers2)
