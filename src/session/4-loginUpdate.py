# parser.py
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어주기
LOGIN_INFO = {
    'userId': 'xxx',
    'userPassword': 'xxx'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # 우선 클리앙 홈페이지에 들어가 봅시다.
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input', {'name': '_csrf'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
    print(csrf['value']) # 위에서 찾은 태그의 value를 가져옵니다.

    # 이제 LOGIN_INFO에 csrf값을 넣어줍시다.
    # (p.s.)Python3에서 두 dict를 합치는 방법은 {**dict1, **dict2} 으로 dict들을 unpacking하는 것입니다.
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
    print(LOGIN_INFO)

    # 이제 다시 로그인을 해봅시다.
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    # 어떤 결과가 나올까요? (200이면 성공!)
    print(login_req.status_code)