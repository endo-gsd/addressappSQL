from menu.menu import MenuAbstract
from person import Person
from message import Messages, MenuName
from judg import Judgement


class Add(MenuAbstract):
    """ アドレス追加機能 """
    def execute_action(self, person_list):
        """ person_list にp を登録
        処理に失敗したとき再度登録をするか選択を表示
        p: Person クラスのインスタンス
        return: y を選択したときADD、それ以外はNone
        """
        judg = Judgement()
        p = Person()
        print(Messages.ADD_FORM)
        p.set_name = input(Messages.INPUT_NAME)
        p.set_tel = input(Messages.INPUT_TEL)

        if judg.name_check(p.name):
            if all([judg.tel_check(p.tel),\
                    not judg.is_registered(\
                    p.name, p.tel, person_list)] ):
                person_list.append(p)
                print(Messages.SUCCESS_ADD)
                return None

        print(Messages.RETRY_SELECT_ADD)
        if Judgement.input_y():
            return MenuName.ADD
        return None
