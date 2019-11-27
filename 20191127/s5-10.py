def product_msg(customers):
    str1 = "Dear "
    str2 = "asdasdsasadsdasdasdassa"
    str3 = 'OK'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg)


members = ['AAA', 'BBB', 'CCC']
product_msg(members)
