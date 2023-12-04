# 忽略证书
import requests
url = "http://bbs.phpwind.net.cn/"
response = requests.get(url, timeout=20, verify = False)
# print(response.content.decode("utf-8"))
print(response.status_code)