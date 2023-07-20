from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
import math

math.factorial(100000)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
# 아무런 경고가 없다면 이상없이 작동되는 것입니다

driver.get(url='https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502')
# 페이지 이동

menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
start = time.time()
# for menu in menus:

urls = []


next_btn = driver.find_element(By.CLASS_NAME, 'next')
next_btn.click()

time.sleep(1)


end = time.time()

print(f"{end - start:.5f} sec")
driver.close()
# 종료
