def build_vip(id, name, tel):
    vip_dict = {'VIP_ID': id, 'Name': name, 'Tel': tel}
    return vip_dict


check = 'Y'
while check != 'N' and check != 'n':
    id = int(input("id = "))
    name = input("name = ")
    tel = input("tel = ")
    print(build_vip(id, name, tel))
    check = input("Continue Y/N = ")

print('End.')
