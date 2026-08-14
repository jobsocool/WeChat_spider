from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Edge()

url = "https://mp.weixin.qq.com/s/k9HF-iFQsfmZbIdoSlb2oQ"

driver.get(url)

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")

content = soup.find("div", id="js_content")

# 提取文字
text = content.get_text("\n", strip=True)

with open("正文.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("正文保存完成")


# 提取图片
images = content.find_all("img")

print("图片数量：", len(images))

for i, img in enumerate(images):
    img_url = img.get("data-src")
    print(i+1, img_url)

driver.quit()