# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) - IP블록 방지(웹브라우저를 통해 접속하는것처럼 보이게 함), 비어있지만 않으면 문제 없음
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장
f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

# <td class="subject">
# <a href="/board/view.php?table=bestofbest>우리나라 지금 현재 전쟁나면 필패인 이유 추가</a><span class="list_memo_count_span"> [18]
# </span>   </td>

        for item in list:
                #에러처리(try ~ catch)
                try:
                        title = item.find("a").text.strip()
                        if re.search("한국", title):
                            print(title)
                            f.write(f"{title}\n")

                except:
                        pass
        
f.close()