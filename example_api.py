import requests
import json
client_id = "XHLMl5ylDi0i4Eq5mQKP"
client_secret = "T5EjTJ72xv"
enc_text = input("번역할 문장을 입력하세요 : ")
#data = "source=ko&target=en&text=" + enc_text
data = {
    "source":"ko",
    "target":"en",
    "text":enc_text
}
url = "https://openapi.naver.com/v1/papago/n2mt"

custom_header = {
    "X-Naver-Client-Id":client_id,
    "X-Naver-Client-Secret":client_secret,
}
req = requests.post(url,headers=custom_header,data=data)

if req.status_code==requests.codes.ok:
    data = json.loads(req.text)
    #print(data['message'])
    print(data['message']['result']['translatedText'])
else:
    print("Error Code:" + str(req.status_code))
