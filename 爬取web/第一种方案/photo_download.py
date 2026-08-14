from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os


driver = webdriver.Edge()

url = "https://mp.weixin.qq.com/s/k9HF-iFQsfmZbIdoSlb2oQ"

driver.get(url)

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")

content = soup.find("div", id="js_content")


# 创建文件夹
if not os.path.exists("文章1"):
    os.mkdir("文章1")


# 保存正文
text = content.get_text("\n", strip=True)

with open("文章1/正文.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("正文保存完成")


# 下载图片
images = content.find_all("img")

print("图片数量：", len(images))


for i, img in enumerate(images):

    img_url = img.get("data-src")

    if img_url:

        try:
            data = requests.get(img_url).content

            with open(f"文章1/图片{i+1}.jpg", "wb") as f:
                f.write(data)

            print("下载完成：图片", i+1)

        except Exception as e:
            print("图片下载失败", i+1, e)


driver.quit()

print("全部完成")