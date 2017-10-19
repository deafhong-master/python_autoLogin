# parser.py
import requests

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP GET Request: requests대신 s 객체를 사용한다.
    req = s.get('https://www.clien.net/service/')
    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    print(html)
    print(header)
    print(status)
    print(is_ok)