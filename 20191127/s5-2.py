nclass = {'週一': ['pytho', 'php'],
          '週二': ['Html15'],
          '週四': ['Javscript', 'nidejs', 'css']
          }

for weekeys, coures in nclass.items():
    print("%s 的課程是: " % weekeys)
# 列印value, 還是串列
    for coure in coures:
        print(coure)
