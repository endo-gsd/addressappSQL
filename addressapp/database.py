import psycopg2


class PostgreConnect:
    """ PostgreSQLのヘルパークラス
    Parameters 
    """
    def __init__(self):
        """ DBの接続情報を保持する
        Parameters
        ----------
        host : ホスト名(str)
        dbname : DB名(str)
        scheme : スキーマ名(str)
        user : ユーザー名(str)
        password : パスワード(str)
        port : ポート(integer)
        """
        self.host = 'localhost'
        self.dbname = 'postgres'
        self.scheme = 'public'
        self.user = 'postgres'
        self.password = 'sqlTraining'
        self.port = 5432

    def __connect(self):
        return psycopg2.connect("host='{0}' port={1} dbname={2} user={3} password='{4}'".format(self.host,self.port,self.dbname,self.user,self.password))
    
    def execute(self, sql):
        """ SQLを実行し、結果を取得する
        sql : 実行したいSQL(str)
        """
        with self.__connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

    def is_existed(self, name, tel):
        self.execute(\
            "CREATE VIEW v_book AS (\
            SELECT B.name, N.tel_number \
            FROM address_books B, tels N\
            WHERE B.tel_id = N.tel_id);\
            SELECT V.name, V.tel_number FROM v_book V\
            WHERE V.name =" + name + "\
            OR V.tel_number =" + tel + ";\
            ")
        self.execute('DROP VIEW v_book;')

    def execute_add(self, name, tel):
        """ 名前と電話番号を登録するSQLを実行
        電話番号が既に存在するときはそのidで登録する"""
        self.execute(\
            "INSERT INTO tels(tel_number) SELECT" + tel +\
            "WHERE NOT EXISTS (SELECT tel_number FROM tels \
                WHERE tel_number = " + tel +");\
        	INSERT INTO address_books(name,tel_id) \
            VALUES (" + name + ", SELECT tel_id FROM tels\
                 WHERE " + tel +" = tel_number));")


    def execute_delete(self, name, tel):
        self.execute('BEGIN;\
            DELETE FROM address_books B\
            WHERE B.name = ' + name +\
            'AND B.tel_id IN(SELECT N.tel_id FROM tels N\
        		WHERE ' + tel + ' = N.tel_number);\
            DELETE FROM tels N\
            WHERE N.tel_id =(SELECT N.tel_id FROM tels N\
        	WHERE N.tel_id NOT IN(\
		        SELECT B.tel_id FROM address_books B));\
            COMMIT;	')

    def execute_list(self):
        rows = self.execute('SELECT B.name, N.tel_number\
            FROM address_books B, tels N\
            WHERE B.tel_id = N.tel_id;')
        return rows

    def execute_search(self, key):
        self.execute(\
            "CREATE VIEW v_book AS (\
            SELECT B.name, N.tel_number \
            FROM address_books B, tels N\
            WHERE B.tel_id = N.tel_id);\
            SELECT V.name, V.tel_number FROM v_book V\
            WHERE V.name LIKE'%'" + key + "'%'\
            OR V.tel_number LIKE'%'" + key + "'%';\
            ")
        self.execute('DROP VIEW v_book;')

    def execute_clear(self):
        """ データベース内のデータをすべて削除するSQLを実行
        id の初期化
        """
        self.execute(\
            "DELETE FROM address_books; DELETE FROM tels;\
            SELECT SETVAL('address_books_book_id_seq', 1, false);\
            SELECT SETVAL('tels_tel_id_seq', 1, false);")
   

posgre = PostgreConnect()
rows = posgre.execute_list
print(rows)