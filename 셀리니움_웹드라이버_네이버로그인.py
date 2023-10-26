# 셀리니움_웹드라이버_네이버로그인.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "[id]"
clipboard.copy(loginID) #ctrl + c
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v') #ctrl + v

loginPW = "[passwd]"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1) #너무빨리 넘어가면 의심

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True: #창이 닫히는 문제 해결
    pass 