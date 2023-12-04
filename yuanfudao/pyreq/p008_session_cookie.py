# 使用seesion保持登录状态，目前暂时会运行失败，后续再查看原因
import requests
url = "https://oa-wmbdcuat.must.edu.mo/cas/login"
code_url = "1111"

data = {
    "username":"ghlong",
    "password":"wemust@Hand888",
    "privacyPolicyId":"on",
    "execution":"e2s3",
    "_eventId":"submit"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Cookie": "SESSION=fed40543-e8b7-44b1-a3e3-1a947f8ef261; isCheckByPrivacy=true"
}
session = requests.session()
session.get(code_url)
r = session.post(url=url,data=data,headers=headers)
print(r.status_code)
print(r.text)