import requests
from bs4 import BeautifulSoup

response = requests.get("https://sce.pccu.edu.tw")
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find_all("img"))
