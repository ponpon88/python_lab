import requests
from bs4 import BeautifulSoup

# 偽裝為瀏覽器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = "https://www.ptt.cc/bbs/Tech_job/index.html"
html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'html.parser')

titles = soup.find_all('div', class_="title", limit=20)

# enumerate 輪詢容器裡的元素
# 或把 i 拿掉
for i, item in enumerate(titles):
    if item.find('a'):
        mystr = item.find('a')
        print('#{}標題: {}\n 連結:http://www.ptt.cc{} '.format(i+1, mystr.string, mystr.get('href')))
