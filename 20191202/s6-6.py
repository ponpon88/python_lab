class Father():
    def hometown(self):
        print('我住在台北')


class Son(Father):
    pass


Frank = Father()
badyFrank = Son()
Frank.hometown()
badyFrank.hometown()
