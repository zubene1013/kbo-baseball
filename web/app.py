#웹 크롤러
# -*- encoding: utf-8 -*-
# pip install bs4

from bs4 import BeautifulSoup
from urllib.request import urlopen, build_opener, HTTPRedirectHandler
from urllib.parse import urlsplit
import ipaddress
import socket
import re

from flask import Flask, render_template, request # pip install flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/action', methods=['GET', 'POST'])
def action():
       
    try:
        # 사용자의 입력정보 받기
        url = request.form['url']
        fileName = request.form['fileName']
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,60}', fileName):
            raise ValueError('파일명은 영문, 숫자, 밑줄, 하이픈만 사용할 수 있습니다.')

        # 메모장 초기화
        fileName = fileName + '.txt'
        f = open('templates/' +fileName, 'w', encoding='utf-8')
        f.write("")
        f.close()


        # 사용자에게 입력값을 받기 / http형태로 처리하기
        first7Chars = url[0:7]
        if (first7Chars != 'http://' and first7Chars != 'https:/'):
            url = 'http://' + url

        # url 파싱 : 컴퓨터가 이해할수 있는 언어로 교체 (url부분으로 인식할수있게)
        parts = urlsplit(url)
        if parts.scheme not in ('http', 'https') or not parts.hostname:
            raise ValueError('HTTP/HTTPS URL만 입력할 수 있습니다.')
        for info in socket.getaddrinfo(parts.hostname, parts.port or (443 if parts.scheme == 'https' else 80), type=socket.SOCK_STREAM):
            ip = ipaddress.ip_address(info[4][0])
            if not ip.is_global:
                raise ValueError('내부망 또는 로컬 주소는 허용되지 않습니다.')
        class NoRedirect(HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None
        url = build_opener(NoRedirect).open(url, timeout=10)

        #html 파싱
        soup = BeautifulSoup(url, 'html.parser')



        # a 태그 추출
        for i in soup.select('a'):
            link = i.get('href', '/')
            first7Chars = link[0:7]

            if (first7Chars != 'http://' and first7Chars != 'https:/'):
                continue

            print(link)
            
            #메모장에 저장
            f = open('templates/' +fileName, 'a', encoding='utf-8') #a는 이어넣기, w는 덮어쓰기
            f.write(link + "\n")
            f.close()

        # 파일 보기 화면으로 이동
        f = open('templates/' +fileName, 'r', encoding='utf-8')
        f = f.readlines()
        print(f)
        return render_template('result.html', f=f, fileName=fileName)

    # 에러처리
    except Exception as log:
        print('에러발생. 원인:', log)
        return render_template('index.html', log=log)
    


if __name__ == '__main__':
    app.run(debug=False)