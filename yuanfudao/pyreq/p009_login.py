# UAT登录获取token
import requests
url = "https://oa-wmbdcuat.must.edu.mo/api/v1/oauth2/accessToken"

data = {
    "username":"ghlong",
    "password":"wemust@Hand888",
    "grantType":"password"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "d21lNDliODE3NzFmNjY0NjMwOmU4NjJkZDIwY2FkMDQ1MTk5ODE2MDI1MWZmYTFmZmVh",

}

# session.get(url)
r = requests.post(url=url,data=data,headers=headers)
res  = r.json()
token = res["model"]["accessToken"]
print(r.status_code)
print(token)
print(res)
