import requests
from bs4 import BeautifulSoup

# 네이버 뷰 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# 해당 URL의 내용을 가져옴
response = requests.get(url)
html = response.text

# BeautifulSoup를 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 블로그 정보가 들어 있는 태그를 찾음
blog_items = soup.find_all("li", class_="sh_blog_top")

# 결과를 저장할 리스트 초기화
results = []

# 블로그 정보를 반복하면서 필요한 데이터 추출
for item in blog_items:
    blog_name = item.find("a", class_="sh_blog_title").text  # 블로그명
    blog_link = item.find("a", class_="sh_blog_title")["href"]  # 블로그 주소
    post_title = item.find("a", class_="sh_blog_title")["title"]  # 글의 제목
    post_date = item.find("dd", class_="txt_inline").text  # 날짜

    result = {
        "Blog Name": blog_name,
        "Blog Link": blog_link,
        "Post Title": post_title,
        "Post Date": post_date,
    }

    results.append(result)

# 결과 출력
for result in results:
    print(result)
