import requests
url = "https://www.sogou.com/web"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
params={
    "query":"python"
}
response = requests.get(url,headers=headers,params=params)
print(response.request.url)
# print(response.content.decode("utf-8"))