from message import Messages
from menu.menu import MenuAbstract


class ListAll(MenuAbstract):
    """ アドレス一覧表示機能 """
    def execute_action(self, person_list):
        """ リストの一覧を表示する
        return: Noneを返す
        """
        print(Messages.LIST_TOP)
        if person_list:
            for person in person_list:
                print(person.name + ' : ' + person.tel)
        else:
            print(Messages.LIST_EMPTY)
        input(Messages.LIST_END)
        return None
