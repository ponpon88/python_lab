class Father():
    def __init__(self):
        self.__address = "台北市建國南路"

    def getaddress(self):
        return self.__address


class Son(Father):
    pass


Frank = Father()
badyFrank = Son()
print('父類別',Frank.getaddress() )
print('子類別',badyFrank.getaddress())
