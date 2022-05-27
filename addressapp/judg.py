import re
from message import Messages


class Judgement:
    """ 判定機能 """
    ANSWER_Y = ('y', 'Y')

    def is_not_empty(self, word):
        """ 空白ではないことを判定 """
        if not(word == '' or word.isspace()):
            return True
        print(Messages.IS_EMPTY)
        return False

    def is_not_tel(self, word):
        """ 電話番号ではないことを判定 """
        if not self.tel_pattern_check(word):
            return True
        print(Messages.NOT_PUT_TEL_IN_NAME)
        return False

    def tel_pattern_check(self, tel):
        """ telが正規表現にマッチするか判定
        tel_pattern: 電話正規表現オブジェクト
        0で始まる半角数字のみの10桁、11桁、
        または半角数字とハイフンで構成された次のいずれか
        (00-0000-0000)(000-000-0000)(0000-00-0000)(000-0000-0000)
        """
        tel_pattern = re. compile(r'''(
        (^0)
        ([0-9]{5,6}
        |[0-9]-[0-9]{4}-
        |[0-9]{2}-[0-9]{3}-
        |[0-9]{3}-[0-9]{2}-
        |[0-9]{2}-[0-9]{4}-)
        ([0-9]{4}$)
        )''', re.VERBOSE)
        if tel_pattern.match(tel):
            return True
        return False

    def is_registered(self, name, tel, person_list):
        """ リストに存在するか判定 """
        if person_list:
            for person in person_list:
                if name == person.name and tel == person.tel:
                    print(Messages.IS_REGISTERED)
                    return True
            return False

    def name_check(self, name):
        """ name の条件に合うか判定 """
        if all([self.is_not_empty(name),
            self.is_not_tel(name)]):
            return True
        return False

    def tel_check(self, tel):
        """ tel の条件に合うか判定 """
        if not self.is_not_empty(tel):
            return False
        if self.tel_pattern_check(tel):
            return True
        print(Messages.IS_NOT_TEL)
        return False

    @classmethod
    def input_y(cls):
        """ input がy かY ならTrue を返す """
        v = input(Messages.BACK_RECEPTION)
        return v in cls.ANSWER_Y
