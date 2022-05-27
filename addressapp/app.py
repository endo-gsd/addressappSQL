import traceback
from file import File
from menu.add import Add
from menu.clear import Clear
from menu.delete import Delete
from menu.listall import ListAll
from menu.quit import Quit
from menu.search import Search
from message import  MenuName, Messages
from form import Form


class App:
    person_list = []

    def __init__(self):
        self.form = Form()
        self.file = File()
        self.menu = {
            MenuName.ADD: Add,
            MenuName.DELETE: Delete,
            MenuName.SEARCH: Search,
            MenuName.LIST: ListAll,
            MenuName.CLEAR: Clear,
            MenuName.QUIT: Quit,
        }

    def call_menu(self, menu):
        """ self.menuから対応するクラスのインスタンスを作成
        execute_actionメソッドを呼び出して戻り値を返す
        self.menuにない場合はNone を返す
        """
        if menu in self.menu:
            menu = self.menu[menu]()
            return menu.execute_action(self.person_list)
        input(Messages.PROMPT_FOR_INPUT)
        return None

    def start_up(self):
        """ アプリケーションの操作 """
        try:
            self.file.read(self.person_list)
            print(Messages.START_UP)
            select = None
            while True:
                menu = self.form.receive(select)
                select = self.call_menu(menu)
        except KeyboardInterrupt:
            print(Messages.CTRL_C_ENTERED)
        except Exception:
            print(traceback.format_exc())
            print(Messages.ERROR)
        finally:
            self.file.close()
            print(Messages.END)
