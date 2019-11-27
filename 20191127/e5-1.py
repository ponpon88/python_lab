def build_vip(id, name, tel=''):
    vip_dict = {'VIP_ID': id, 'Name': name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict


a = build_vip('101', 'Frank')
b = build_vip('102', 'Pon', '123')
print(a)
print(b)
