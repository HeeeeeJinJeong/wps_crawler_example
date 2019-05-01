import requests
import json

url = "http://finance.daum.net/api/quote/A048410/days?symbolCode=A048410&page=1&perPage=10"

custom_headers = {'referer':'http://finance.daum.net/api/quote/A048410/days?symbolCode=A048410&page=1&perPage=10', 'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

req = requests.get(url, headers=custom_headers)

if req.status_code == requests.codes.ok:
    print('접속 성공')
    # 데이터 해석
    stock_data = json.loads(req.text)
    print(stock_data['data'])
    for daily_data in stock_data['data'][:5]:
        print(daily_data['date'], daily_data['tradePrice'])
else:
    print('접속 실패')