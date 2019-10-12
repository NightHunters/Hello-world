# 需要调用的requests 库和 BeautifulSoup库中的bs4工具
import requests
import soup as soup
from bs4 import BeautifulSoup

num = 0  # 定义条数的初始值
# 定义一个变量url，为需要爬取数据的网页网址
url = 'https://github.com/microsoft/vscode/issues'
# 获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'})
# 生成一个Beautifulsoup对象，用以后边的查找工作
soup = BeautifulSoup(req.text, 'html.parser')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
xml = soup.find_all('a',class_='link-gray-dark v-align-middle no-underline h4 js-navigation-open')

# 利用循环将xml[]中存放的每一条打印出来

for i in range(len(xml)):  # 表示从0到xml的len()长度
    msg = xml[i].string
    if not msg is None:
        num += 1
    print('第', num, '条', msg)
