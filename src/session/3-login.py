# parser.py
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어주기
LOGIN_INFO = {
    'userId': 'xxx',
    'userPassword': 'xxx'
}

# Session 생성 with 구문 안에서 유지되도록 로직 짜기
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url 와 함께 전송될 data 를 넣어주기.
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    # 어떤 결과가 나올까.?
    print(login_req.status_code)