import requests
import urllib.request
import json

client_id = "ruRpQhAc13Y2SFMnO1K4" # 개발자센터에서 발급받은 Client ID 값
client_secret = "uY_HzzwTO8" # 개발자센터에서 발급받은 Client Secret 값

custom_header={"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}

encText = urllib.parse.quote("https://developers.naver.com/docs/utils/shortenurl")
data = "url=" + encText

url = "https://openapi.naver.com/v1/util/shorturl"
req = requests.post(url, headers=custom_header, data=data)


if req.status_code == requests.codes.ok:
    print('접속 성공')
    url_data=json.loads(req.text)
    # print(url_data['message']['result']['translatedText'])


# encText = "안녕?" # input("번역할 문장을 입력하세요 : ")
# # data = "source=ko&target=en&text=" + encText
# data = {"source":"ko","target":"en","text":encText}

