# web1.py
#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
page = open("C:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체 보기
print(soup.prettify())

