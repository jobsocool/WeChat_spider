from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os


# 文章链接
url = "https://mp.weixin.qq.com/s/k9HF-iFQsfmZbIdoSlb2oQ"


# 创建浏览器
driver = webdriver.Edge()

driver.get(url)

# 等待网页加载
time.sleep(5)


# 获取完整网页
html = driver.page_source

soup = BeautifulSoup(html, "lxml")


# 获取正文
content = soup.find("div", id="js_content")

if content is None:
    print("没有找到正文")
    driver.quit()
    exit()


# 创建保存目录
folder = "文章1"

if not os.path.exists(folder):
    os.mkdir(folder)


# 下载图片并修改HTML中的图片地址
images = content.find_all("img")

print("发现图片数量：", len(images))


for i, img in enumerate(images):

    img_url = img.get("data-src")

    if img_url:

        try:
            img_data = requests.get(img_url).content

            img_name = f"图片{i+1}.jpg"

            img_path = os.path.join(folder, img_name)

            with open(img_path, "wb") as f:
                f.write(img_data)

            # 修改HTML图片路径
            img["src"] = img_name

            print("下载完成：", img_name)

        except Exception as e:
            print("图片下载失败：", i+1, e)


# 生成HTML
title = soup.title.text if soup.title else "微信公众号文章"

html_page = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>

<style>
body {{
    max-width: 800px;
    margin: auto;
    font-size: 18px;
    line-height: 1.8;
}}

img {{
    max-width: 100%;
}}
</style>

</head>

<body>

<h1>{title}</h1>

{content}

</body>

</html>
"""


# 保存HTML
html_path = os.path.join(folder, "index.html")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_page)


driver.quit()


print("\n全部完成！")
print("打开：文章1/index.html")