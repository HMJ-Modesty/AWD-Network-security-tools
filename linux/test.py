import requests
import urllib3


urllib3.disable_warnings()

headers1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie" : "think_lang=zh-cn; autoLogin=ko9auYND2C02hQQsxG98rnS9Z0dSe7yDR6WKRQeMjN4RCuAQkGMdGTGaWMD9/3gx7QWuv3q6aqzHz8QEYa/em+89QF5KTnupVlhaALorwkcELDgh9ssC1ESxYg3MrF6wShBy; X-CSRF-TOKEN=02e8eb310a3cafbe01f92bbf795ede23; PHPSESSID=62c68db8133fb8f247da1514a5fa14e6"
}

headers2 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie" : "think_lang=zh-cn; PHPSESSID=62c68db8133fb8f247da1514a5fa14e6; autoLogin=xI1Q74QR23k2hQQsxG98rnS9Z0dSe7yDRq2JSwqMjN4RCuAQkGMdGTGaWMD8+3gx40G9vnGta6KSnZUKa+GP2LpjTlMcH3r+VgAeWvglk0sEZCJ8rNMb1BfiNg2WsgXqUgludbEVzG2n; X-CSRF-TOKEN=6aeff5742287362927aaf81adc408684"
}

def checkin(headers):
    a = requests.get("https://ctf.bugku.com/", headers=headers, verify=False, timeout=40)
    info = requests.get("https://ctf.bugku.com/user/checkin", headers=headers, verify=False, timeout=40).text.split(
        '<h3 class="m-t-30">')[1].split('</')[0]
    print(info.strip())

checkin(headers1)
checkin(headers2)