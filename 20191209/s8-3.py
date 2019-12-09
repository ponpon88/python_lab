import requests
from bs4 import BeautifulSoup

# 偽裝為瀏覽器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

response = requests.get("https://sce.pccu.edu.tw", headers=header)
response.encodeing = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find_all("img"))
