from judg import Judgement
from message import Messages, MenuName
from menu.menu import MenuAbstract


class Search(MenuAbstract):
    """ アドレス検索機能 """
    def execute_action(self, person_list):
        """ 未入力をチェック後、リストから文字を探して一致するデータを表示
        key: 検索したい文字や数字
        return: y を入力時SEARCH、それ以外はNoneを返す
        """
        print(Messages.SEARCH_FORM)
        key = input(Messages.INPUT_KEY)
        if key:
            found = False
            for person in person_list:
                if key in person.name or key in person.tel:
                    found = True
                    print(person.name + ' : ' + person.tel)
            if not found:
                print(Messages.NOT_FOUND)
        else:
            print(Messages.KEY_IS_EMPTY)

        print(Messages.RETRY_SELECT_SEARCH)
        if Judgement.input_y():
            return MenuName.SEARCH
        return None
