import requests

# 偽裝為瀏覽器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'
htmlfile = requests.get(url, headers=header)
fn = 'out2.html'
with open(fn, 'wb') as file_Obj:
    for diskstorge in htmlfile.iter_content(10240):
        size = file_Obj.write(diskstorge)
        print(size)
    print("以 %s 儲存網頁" % size)
