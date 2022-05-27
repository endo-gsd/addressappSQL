from judg import Judgement
from message import Messages, MenuName
from menu.menu import MenuAbstract


class Delete(MenuAbstract):
    """ アドレス削除機能 """
    def execute_action(self, person_list):
        """ リストの中からキーワードと完全に一致するデータを削除する
        処理が失敗したとき再度削除を行う選択を表示する
        delete_name: 削除したい名前
        delete_tel: 削除したい電話番号
        return: y を入力されたときにDELETE、それ以外はNone
        """
        print(Messages.DELETE_FORM)
        delete_name = input(Messages.INPUT_NAME)
        delete_tel = input(Messages.INPUT_TEL)
        for person in person_list:
            if delete_name == person.name \
                and delete_tel == person.tel:
                person_list.remove(person)
                print(Messages.SUCCESS_DELETE)
                return None

        print(Messages.RETRY_SELECT_DELETE)
        if Judgement.input_y():
            return MenuName.DELETE
        return None
