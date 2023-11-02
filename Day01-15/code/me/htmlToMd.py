# 1. 获取整个页面数据
import requests
import kuser_agent

url = 'https://zhuanlan.zhihu.com/p/377552129#:~:text=5%20linux%20%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85MySQL%201%201%EF%BC%89%20%E5%8D%B8%E8%BD%BDCentOS7%E7%B3%BB%E7%BB%9F%E8%87%AA%E5%B8%A6mariadb%20...%202,7%EF%BC%89%20%E5%BC%80%E5%A7%8B%E5%AE%89%E8%A3%85MySQL%20...%208%208%EF%BC%89%20%E5%90%AF%E5%8A%A8MySQL%20...%20%E6%9B%B4%E5%A4%9A%E9%A1%B9%E7%9B%AE'
html = requests.get(url=url, headers={'User-Agent': kuser_agent.get()}).content

# 2. 提取正文中的HTML文本
from bs4 import BeautifulSoup

bs = BeautifulSoup(html)
text = bs.find(attrs={'id': 'article_content'}).prettify()

# 3. 将HTML文本转成Markdown格式
import html2text

ht = html2text.HTML2Text()
# 一般的参数设置
ht.bypass_tables = False
ht.mark_code = True
ht.code = True
# --------------
result = ht.handle(text)
print(result)
