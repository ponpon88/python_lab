import requests

url = 'https://sce.pccu.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))
print(htmlfile.status_code)

print(htmlfile.text)
''''
try:
    url2 = 'https://www.test222.com/abcde'
    htmlfile2 = requests.get(url2)
    print("Success")
except Exception as err:
    print("Error: %s" % err)
'''

# 偽裝為瀏覽器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url3 = 'https://www.ntu.edu.tw'
htmlfile3 = requests.get(url3, headers=header)
print(htmlfile3.status_code)
#text = htmlfile3.text
#print(text)

fn = 'out.html'
with open(fn,'wb') as file_Obj:
    for diskstorge in htmlfile3.iter_content(10240):
        size = file_Obj.write(diskstorge)
        print(size)
    print("以 %s 儲存網頁" % size)
