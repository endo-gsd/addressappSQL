from message import Messages

class Form:
    """ 受付フォーム """
    def receive(self, select):
        """ 入力を仕分けする
        select がNone ならば文字を入力
        select に合うクラスを返す、合わない時はNone を返す
        """
        if select is None:
            print(Messages.MENU)
            select = input(Messages.SELECT_MENU)
        menu = select
        return menu
