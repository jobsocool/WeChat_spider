WeChat_spider
自动分类文件夹 保存 HTML 排版 下载图片 数据库搜索 搜索结果显示摘要

#提示:请安装edge浏览器，此工具爬取时需要edge浏览器

###项目定位：
一个基于 Selenium + BeautifulSoup + SQLite 的微信公众号文章本地采集与全文检索工具，主要用于个人资料整理与关键词检索。

1. 项目简介
本项目用于采集指定微信公众号的文章，并将文章内容、图片和 HTML 排版保存到本地。
在采集完成后，建立本地数据库，实现关键词搜索文章的功能。
主要用途：个人资料整理与检索。
2. 当前需求
目标是采集指定微信公众号的最近 100 篇文章。
每篇文章需要：
[x] 获取文章正文
[x] 下载文章中的图片
[x] 保存 HTML 页面
[x] 自动分类保存文件
[ ] 建立 SQLite 数据库
[ ] 关键词搜索
[ ] 搜索结果显示文章摘要
3. 技术方案
#网页访问
使用：
Selenium
控制 Microsoft Edge 浏览器访问微信公众号文章。
#HTML 解析
使用：
BeautifulSoup4
lxml
解析文章 HTML。
#图片下载
使用：
requests
下载文章中的图片。
#数据库
计划使用：
SQLite
保存文章信息并实现关键词搜索。
4. 为什么不用 requests 直接爬取？
最开始使用：
requests.get()
访问微信公众号文章。
虽然返回：
状态码：200
但实际返回的是微信的环境检测页面：
环境异常
当前环境异常，完成验证后即可继续访问。
页面中没有正常的：
js_content
msg_title
因此无法直接提取文章正文。
后来改用 Selenium 控制 Edge浏览器
#因为没有安装chorme所以使用edge
6. Selenium 方案
使用：
from selenium import webdriver

driver = webdriver.Edge()

driver.get(url)
让 Edge 像正常浏览器一样打开微信公众号文章。
成功后：
html = driver.page_source
获取完整网页源码。
测试结果：
requests 获取网页：
18044 字符

Selenium 获取网页：
4064425 字符
说明 Selenium 成功获取到了完整页面。
6. 正文提取
微信公众号文章正文位于：
HTML
<div id="js_content">
使用 BeautifulSoup：
content = soup.find("div", id="js_content")
然后：
text = content.get_text("\n", strip=True)
成功提取正文。
7. 图片提取
微信公众号文章中的图片链接主要通过：
HTML
data-src
获取。
Python：
images = content.find_all("img")

for img in images:
    img_url = img.get("data-src")
测试文章成功识别：
图片数量：11
并成功下载了大部分图片。
8. HTML 保存
文章不仅保存为 TXT，还保存为：
index.html
HTML 中保留：
正文
图片
基本排版
同时将网络图片下载到本地，并修改 HTML 中的图片路径，使 HTML 可以脱离网络查看。
9. 文件结构
计划使用类似：
文章库/
│
├── 2026-08-14_文章标题1/
│   ├── index.html
│   ├── 正文.txt
│   └── images/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── 3.jpg
│
├── 2026-08-13_文章标题2/
│   ├── index.html
│   ├── 正文.txt
│   └── images/
│       └── ...
│
└── ...
这样每篇文章独立保存，方便管理。
10. 数据库设计
计划使用 SQLite。
例如：
articles
├── id
├── title
├── publish_time
├── url
├── content
└── file_path
这样就可以通过数据库快速搜索，而不用每次重新读取所有 HTML 文件。
11. 搜索功能
目标：
输入：
芯片
返回：
找到 8 篇文章

1. AI芯片行业分析
   发布时间：2026-08-10
   摘要：今年芯片行业出现……

2. 科技硬件市场分析
   发布时间：2026-08-08
   摘要：近期科技硬件板块……
搜索结果可以点击或打开对应的：
index.html
查看完整文章。
12. 最终工作流程
输入公众号文章
        ↓
获取文章链接
        ↓
Selenium + Edge
        ↓
打开文章
        ↓
获取完整 HTML
        ↓
BeautifulSoup 解析
        ↓
┌───────────────┐
│ 标题          │
│ 正文          │
│ 图片          │
│ 发布时间      │
│ 原文章链接    │
└───────────────┘
        ↓
自动建立文章文件夹
        ↓
保存 HTML + 图片
        ↓
写入 SQLite
        ↓
关键词搜索
        ↓
返回文章 + 摘要
13. 已完成
目前已经成功实现：
[x] 安装 Python 爬虫相关库
[x] requests 测试
[x] 发现微信公众号环境检测
[x] 安装 Selenium
[x] 使用 Edge
[x] Selenium 成功打开微信公众号文章
[x] 获取完整 HTML
[x] 找到 js_content
[x] 提取正文
[x] 获取图片链接
[x] 下载图片
[x] 保存文章
[x] 生成 HTML
[x] 本地图片与 HTML 一起保存
[x] ZIP 打包后可以交给其他人使用
###遇到的问题##%
问题1：requests 返回环境异常
解决：
requests
失败
Selenium + Edge
成功
问题2：文件命名冲突
因将Python文件命名为：
html.py
导致 BeautifulSoup 导入失败。
原因：
html.py
与 Python 自带的html模块冲突。
解决：
改成wechat_html.py
同时删除：
__pycache__
15. 后续开发计划
第一阶段
[x] 单篇文章采集
[x] 图片下载
[x] HTML 保存
第二阶段
[ ] 自动获取最近100篇文章
[ ] 批量采集
[ ] 自动分类
[ ] 自动命名
第三阶段
[ ] SQLite 数据库
[ ] 关键词搜索
[ ] 搜索结果摘要
[ ] 显示文章发布时间
[ ] 打开对应 HTML
第四阶段
可以考虑做一个简单 GUI：
┌──────────────────────────┐
│ 微信公众号文章资料库      │
│                          │
│ 搜索： [      芯片      ] │
│                          │
│ [搜索]                   │
│                          │
│ 找到 8 篇文章             │
│                          │
│ ① AI芯片行业分析         │
│   ……芯片行业……          │
│                          │
│ ② 科技硬件市场分析       │
│   ……芯片市场……          │
└──────────────────────────┘
这样最终就从一个爬虫脚本升级成一个真正的本地微信公众号资料检索工具。
依赖库
目前使用：
pip install requests beautifulsoup4 lxml selenium
后续如果需要 GUI / 数据处理，可以再增加相应依赖。
