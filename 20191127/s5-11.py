def product_msg(*customers):
    for customer in customers:
        print('---', customer)


product_msg('AAA', 'BBB', 'CCC')
