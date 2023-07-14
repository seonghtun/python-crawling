from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
# 아무런 경고가 없다면 이상없이 작동되는 것입니다

driver.get(url='https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502')
# 페이지 이동

menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
list(menus)[0].click()
print(driver.current_url)
# print(driver.page_source)
driver.back()
# 이동되었는지 확인

time.sleep(2)

driver.close()
# 종료
