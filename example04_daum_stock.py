"""
메뉴 1 : 조회 급등 항목 10개의 현재가 출력
메뉴 2 : 1) 종목 코드를 입력받고, 2) 해당 종목의 1페이지 추가 출력
메뉴 2-1 : 데이터 엑셀로 저장하기

1. 메뉴 구현하기
2. 1번 메뉴에 대한 크롤러
  - 조회 급등 항목 10개 찾기
  - 그 항목 1개에 대한 데이터 찾아서 출력
  - 총 10개 항목에 대한 데이터 찾아서 출력
3. 2번 메뉴에 대한 크롤러
  - 아무 항목이나 1페이지 추가 출력
  - 사용자에게 종목 코드 입력받아서 출력하기
"""
import requests
import json


url = "http://finance.daum.net/api/search/ranks?limit=10"

custom_headers = {'referer':'http://finance.daum.net/quotes/A048410#current/quote', 'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

req = requests.get(url, headers=custom_headers)

if req.status_code == requests.codes.ok:
    print('접속 성공')
    # print(req.text)

    rank_data = json.loads(req.text)
    for rank in rank_data['data']:
        print(rank['rank'],rank['name'],rank['symbolCode'])

else:
    print('접속 실패')