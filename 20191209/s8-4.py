import bs4

htmlfile = open('20191209/sample.html', encoding="utf-8")
soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
mytag = soup.select('li')
print("li count as:", len(mytag))
print(mytag)
for con in mytag:
    print(con)

p4_class = soup.select(".p-4")
print("p-4 count as:", len(p4_class))
print(p4_class)

p_tag = soup.find_all('p', class_='mb-0')
print("p-4 by find all count as", len(p_tag))
print(p_tag)

a_tag = soup.select("#link2")
print(a_tag[0]['id'])
print(a_tag[0]['href'])
# 回傳所有屬性
print(soup.a.attrs)
