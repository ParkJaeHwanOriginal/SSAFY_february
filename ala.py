import requests
import json

API_URL = 'http://127.0.0.1:8000'
API_KEY = 'ttbpogpog12301450001'

url = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=50&start=1&SearchTarget=Book&output=JS&Version=20131101'

response = requests.get(url)

# JSON 문자열을 파이썬 딕셔너리로 변환
data = response.json()

# item 필드 추출
items = data.get('item')

for i in items : 
    print(i['isbn13'])
    print(i['author'])
    print(i['title'])
    print(i['pubDate'])

# 추출한 item 출력
# print(items)


