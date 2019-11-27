def make_food(food_type, *things):
    print("This ", food_type, " need ")
    for thing in things:
        print('---', thing)


make_food('111', '222', '333')
make_food('AAA', 'BBB', 'CCC')
