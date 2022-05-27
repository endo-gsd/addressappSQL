class Person:
    """ 名前と電話番号を結びつけた個人 """
    def __init__(self, name='', tel=''):
        """ name, tel のインスタンス変数の作成 """
        self.__name = name
        self.__tel = tel

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def set_tel(self, tel):
        self.__tel = tel
