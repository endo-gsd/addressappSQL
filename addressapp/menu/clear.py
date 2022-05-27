from judg import Judgement
from message import Messages
from menu.menu import MenuAbstract


class Clear(MenuAbstract):
    """ アドレス初期化機能 """
    def execute_action(self, person_list):
        """ リストのデータを削除する
        y を入力時にリストの初期化を実行する
        return: None を返す
        """
        print(Messages.CONFIRM_CLEAR)
        if Judgement.input_y():
            person_list.clear()
            print(Messages.SUCCESS_CLEAR)
        else:
            input(Messages.BREAK_CLEAR)
        return None
