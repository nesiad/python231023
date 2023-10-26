import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Set the headers for the Excel file
sheet.append(["Blog Name", "Blog Link", "Post Title", "Post Date"])

# 1페이지에서 100페이지까지 반복
for page in range(1, 101):
    # 네이버 뷰 검색 결과 페이지 URL (페이지 번호 동적으로 변경)
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81&start={page * 10}"

    # 해당 URL의 내용을 가져옴
    response = requests.get(url)
    html = response.text

    # BeautifulSoup를 사용하여 HTML 파싱
    soup = BeautifulSoup(html, "html.parser")

    # 블로그 정보가 들어 있는 태그를 찾음
    blog_items = soup.find_all("li", class_="sh_blog_top")

    # 블로그 정보를 반복하면서 필요한 데이터 추출
    for item in blog_items:
        blog_name = item.find("a", class_="sh_blog_title").text  # 블로그명
        blog_link = item.find("a", class_="sh_blog_title")["href"]  # 블로그 주소
        post_title = item.find("a", class_="sh_blog_title")["title"]  # 글의 제목
        post_date = item.find("dd", class_="txt_inline").text  # 날짜

        # Add the data to the Excel sheet
        sheet.append([blog_name, blog_link, post_title, post_date])

# Save the results to an Excel file with a specific path
file_path = "C:\\work\\result.xlsx"
workbook.save(file_path)
