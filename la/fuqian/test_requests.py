import requests

r = requests.get('https://www.baidu.com/')  # 豆瓣首页
print(r.status_code)
print(r.text)
