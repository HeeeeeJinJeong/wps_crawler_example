# 웹 페이지에 접근해서 데이터를 가져온다.
# requests는 aiax로 받아온 데이터를 실시간으로 반영할 수 있다.
# requests로 받아온 데이터는 소스보기에서 보는 소스까지만 있다.

# selenium : 웹 브라우저를 원격 조작하는 방식의 크롤러
# selenium, scrapy

import requests

# 가져온 데이터를 HTML로 해석한다.
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

# HTTP Method : Get, Post, Put, Head, Delete
# Get : 리소스 얻기
# Post : 데이터 전달 - 로그인, 회원가입, 글쓰기 ... -------------- 수정
# Put : 리소스 전달 - 사진 올리기 ---------------- 최초 업로드
# Delete : 리소스 삭제
# Head : Method 확인
# Postman 이라는 익스텐션 설치

req = requests.get(url)
# print(req.status_code)
# print(type(req.status_code))

if req.status_code == requests.codes.ok:
    print('접속 성공')
    # 데이터 해석
    # print(req.text)
    html = BeautifulSoup(req.text, "html.parser")
    items = html.select('.PM_CL_realtimeKeyword_list_base .ah_item')

    # 어떤 요소를 찾고 그 요소 안에 각각의 요소를 다시 찾을 수 있다.
    # 순위와 키워드, 링크 같이 찾기
    for item in items:
        keyword = item.select_one('.ah_k')
        rank = item.select_one('.ah_r')
        link = item.select_one('a.ah_a')

        print(rank.text, keyword.text, link.attrs['href'])

    # keywords = html.select('.PM_CL_realtimeKeyword_list_base .ah_k')
    # ranks = html.select('.PM_CL_realtimeKeyword_list_base .ah_item')

else:
    print('접속 실패')

