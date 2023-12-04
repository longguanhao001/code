import requests
url = "https://way.jd.com/he/freeweather"
data = {
    "appkey":"f0916011eed473059daf0d9ed334fb07",
    "city":"广州"
}
response = requests.post(url=url, data=data)

print(response.status_code)
print(type(response.text))
res = response.json()
print(type(res))
print(res["msg"])
print(res)

