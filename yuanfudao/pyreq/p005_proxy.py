import requests
url = "https://www.google.com/"
proxies={
    "http":"http://61.216.185.88:60808"
}
response = requests.get(url, timeout=20, proxies = proxies)
print(response.content.decode("utf-8"))