#dict
# name_dict = { key1:value1 .... keyn:valuen,}

fruits = {'西瓜': 15,'香蕉': 20, '芭樂': 25}
noodles = {'牛肉麵':100, '雜醬麵':80, '陽春麵':60}
print(fruits)
print(noodles)

print('芭樂一斤:',fruits['芭樂'])

fruits['橘子'] = 18
print(fruits)
key = input('Pls input key = ')
value = input('Pls input value = ')
if key in fruits:
    print('%s 已存在' %key)
else:
    fruits[key] = value
    print('新增',fruits)
