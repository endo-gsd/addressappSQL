class MenuName:
    ADD = 'add'
    DELETE = 'delete'
    SEARCH = 'search'
    LIST = 'list'
    CLEAR = 'clear'
    QUIT = 'quit'


class Messages:
    """ 表示されるメッセージの管理 """
    START_UP = '電話帳アプリケーションが起動しました。'
    MENU = '\n[ 受付フォーム ]\n\n登録: ' + MenuName.ADD \
            + '  削除: ' + MenuName.DELETE \
            + '  一覧表示: ' + MenuName.LIST \
            + '  検索: ' + MenuName.SEARCH \
            + '  初期化: ' + MenuName.CLEAR\
            + '  終了: '+ MenuName.QUIT + '\n'
    SELECT_MENU = '上記の英語を入力して選択してください:'
    PROMPT_FOR_INPUT = 'Enter で受付に戻り、もう一度入力してください:'
    BACK_RECEPTION = '(その他は受付に戻ります):'
    INPUT_NAME = '名前を入力してください：'
    INPUT_TEL = '電話番号を入力してください(半角数字):'
    ADD_FORM = '\n[ 登録フォーム ]\n'
    IS_EMPTY = '入力されていない項目があります。'
    NOT_PUT_TEL_IN_NAME  = '名前に電話番号を登録することはできません。'
    IS_NOT_TEL = '電話番号が入力条件に合いませんでした。'
    IS_REGISTERED = '既に登録されています。'
    SUCCESS_ADD = '登録しました。'
    DELETE_FORM = '\n[ 削除フォーム ]\n'
    SUCCESS_DELETE = '削除しました。'
    LIST_TOP = '\nリスト一覧\n----------------------------'
    LIST_EMPTY = 'リストは空です。'
    LIST_END = '----------------------------\n受付へ戻るにはEnter を押してください:'
    SEARCH_FORM = '\n[ 検索フォーム ]\n'
    INPUT_KEY = '検索を行いたい文字を入力してください。:'
    KEY_IS_EMPTY = '入力されていません。'
    NOT_FOUND = '検索された条件が見つかりませんでした。'
    CONFIRM_CLEAR ='本当に全てのデータを削除しますか？\nyで削除します'
    SUCCESS_CLEAR = 'データをすべて削除しました。'
    BREAK_CLEAR = '削除を取りやめました。Enter を押してください:'
    CONFIRM_QUIT = 'アプリケーションを終了しますか？\nyで終了します'
    FILE_NOT_OPEN = 'ファイルの読み込みに失敗しました。\n問題が発生しました。終了します。'
    FAILED_READ_FILE = 'ファイルの読み込みに失敗しました。'
    ERROR = '問題が発生しました。'
    CTRL_C_ENTERED = '\nCtrl+Cが入力されました。'
    END = '終了します。'
    RETRY_SELECT_ADD = '\n入力した情報が条件に合わなかったため、登録に失敗しました。\n再度登録を行うにはy を入力'
    RETRY_SELECT_DELETE = '\n入力した文字に合うデータが無かったため、削除に失敗しました。\n再度削除を行うにはy を入力'
    RETRY_SELECT_SEARCH = '\n再度検索を行うにはy を入力'
