# import requests
# import json

# API_URL = 'http://127.0.0.1:8000'
# API_KEY = 'ttbpogpog12301450001'

# url = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=Bestseller&MaxResults=50&start=1&SearchTarget=Book&output=JS&Version=20131101'

# response = requests.get(url)

# # JSON 문자열을 파이썬 딕셔너리로 변환
# data = response.json()

# # item 필드 추출
# items = data.get('item')

# lst = []
# for i in items : 
#     dic = dict()
#     dic['국제 표준 도서 번호'] = i['isbn13']
#     dic['저자'] = i['author']
#     dic['제목'] = i['title']
#     dic['출간일'] = i['pubDate']
#     lst.append(dic)
# print(lst)

dic = [ { 'asdf' : 2, 'asd' : 4}, { 'asdf' : 6, 'asd' : 9 } ]
dic = sorted(dic, key=lambda x: x['asd'], reverse=True )
print(dic)