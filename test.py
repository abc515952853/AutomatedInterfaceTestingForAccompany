import requests
import  json 

url = "https://appgateway.qianjifang.com.cn/connect/token"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}
# payload = "client_id=app&grant_type=phone_number_token&client_secret=2e410faa120546b1922d36379bde2c8d&phone_number=11400000000&verification_token=320098&undefined="
payload = {
    "client_id":"app",
    "grant_type":"phone_number_token",
    "client_secret":"2e410faa120546b1922d36379bde2c8d",
    "phone_number":"11400000000",
    "verification_token":"320098"
}

r = requests.post(url=url,data=json.dumps(payload),headers = headers)
print(r.status_code,r.text)




