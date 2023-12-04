
import requests
url = "https://www.baidu.com/"
# url = "https://www.jd.com/"
response = requests.get(url)
print(response.status_code)


# 打印文本，可能会乱码
# print(response.text)
# 解决乱码的问题
print(response.content.decode("utf-8"))