from selenium import webdriver
from selenium.webdriver.common.by import By

browser =webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME,"link_login")
elem
elem.click()
browser.back() # 뒤로가기
browser.forward() # 앞으로 가기
browser.refresh() # 새로고침
elem = browser.find_element(By.ID,"query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("구글")
elem.send_keys(Keys.ENTER)