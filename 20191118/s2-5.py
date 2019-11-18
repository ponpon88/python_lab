# 覆寫檔案
fs1 = open("20191118/sample-1.txt", mode="w", encoding='utf-8')
print("這是要覆寫資料的內容111", file=fs1)

fs1 = open("20191118/sample-2.txt", mode="a", encoding='utf-8')
print("這是要覆寫資料的內容222", file=fs1)
