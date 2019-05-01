import requests

# 가져온 데이터를 HTML로 해석한다.
from bs4 import BeautifulSoup

# URL Encoding
# URL Decoding
url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90+%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

custom_headers = {'referer':'https://www.naver.com/', 'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

req = requests.get(url, headers=custom_headers)

if req.status_code == requests.codes.ok:
    print('접속 성공')
    # 데이터 해석
    html = BeautifulSoup(req.text, "html.parser")
    numbers = html.select('.num_box .num')

    # 로또 당첨번호 출력하기
    for number in numbers[:6]:
        print(number.text, end=", ")
    print("보너스 번호 : ", numbers[-1].text)
else:
    print('접속 실패')