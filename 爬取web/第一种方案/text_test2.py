from selenium import webdriver
import time

driver = webdriver.Edge()

url = "https://mp.weixin.qq.com/s/k9HF-iFQsfmZbIdoSlb2oQ"

driver.get(url)

time.sleep(5)

html = driver.page_source

print("网页长度：", len(html))

print(html[:500])

driver.quit()