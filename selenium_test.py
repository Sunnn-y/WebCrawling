from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('detach', True) #브라우저 바로꺼짐 방지

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://n.news.naver.com/mnews/article/030/0003154414?sid=101')
driver.implicitly_wait(10) # 열릴 때까지 10초 기다리기

print(driver.find_element(By.CSS_SELECTOR, "h2#title_area").text)

# time.sleep(5) # 5초동안 코드 멈춤
# for li in driver.find_elements(By.CSS_SELECTOR, "li.u_likeit_list"):
#     print(li.find_element(By.CSS_SELECTOR, ".u_likeit_list_name").text)
#     print(li.find_element(By.CSS_SELECTOR, ".u_likeit_list_count").text)

# time.sleep(10) # 10초동안 코드 멈춤

driver.find_element(By.CSS_SELECTOR, ".Nicon_search").click() # get_attribution 도 있음
driver.find_element(By.CSS_SELECTOR, "._search_input").send_keys("삼성전자")
driver.find_element(By.CSS_SELECTOR, ".u_hssbt_us._total_search_btn ").click()

# input("Press Enter to close the browser...")  # 브라우저가 닫히지 않도록 대기합니다.
# driver.quit()  # 브라우저를 닫습니다.

