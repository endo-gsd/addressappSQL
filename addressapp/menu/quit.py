from judg import Judgement
from message import Messages
from file import File
from menu.menu import MenuAbstract


class Quit(MenuAbstract):
    """ 終了機能 """
    def execute_action(self, person_list):
        """ ファイルを書き込み終了する
        y を入力時実行される
        """
        file = File()
        print(Messages.CONFIRM_QUIT)
        file.write(person_list)
        if Judgement.input_y():
            exit()
        else:
            return None
