from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Edge()

url = "https://mp.weixin.qq.com/s/k9HF-iFQsfmZbIdoSlb2oQ"

driver.get(url)

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")


# 查找正文
content = soup.find("div", id="js_content")

if content:
    print("找到正文！")

    text = content.get_text("\n", strip=True)

    print(text[:1000])

else:
    print("没有找到正文")


driver.quit()