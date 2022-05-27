import psycopg2


class PostgreConnect:
    """ PostgreSQLのヘルパークラス
    Parameters 
    """
    GET_TABLE_LIST_QUERY = "SELECT t.* FROM (SELECT TABLENAME,SCHEMANAME,'table' as TYPE from PG_TABLES UNION SELECT VIEWNAME,SCHEMANAME,'view' as TYPE from PG_VIEWS) t WHERE TABLENAME LIKE LOWER('{0}') and SCHEMANAME like LOWER('{1}') and TYPE like LOWER('{2}')"
    GET_COLUMN_LIST_QUERY = "SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME like LOWER('{0}') and TABLE_SCHEMA like LOWER('{1}') ORDER BY ORDINAL_POSITION"
    GET_ALTER_TABLE_QUERY = "ALTER TABLE {0} ADD {1}"
    GET_RENAME_TABLE_QUERY = "alter table {0} rename to {1}"
    
    def __init__(self,host,dbname,scheme,user,password,port=5432):
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
        self.host = host
        self.dbname = dbname
        self.scheme = scheme
        self.user = user
        self.password = password
        self.port = port

    def __connect(self):
        return psycopg2.connect("host='{0}' port={1} dbname={2} user={3} password='{4}'".format(self.host,self.port,self.dbname,self.user,self.password))
    
    def execute(self,sql):
        """ SQLを実行し、結果を取得する
        Parameters
        ----------
        columns : 実行したいSQL(str)           
        """
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
       
    def execute_all(self,sqls):
        """ 複数のSQLをトランザクション配下で実行する
        Parameters
        ----------
        columns : 実行したいSQLのリスト(strs)
        """
        conn = self.__connect()
        cur = conn.cursor()
        try:
            for sql in sqls:
                cur.execute(sql)
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
        cur.close()
        conn.close()
    
    def execute_query(self,sql):
        """ select 系のSQLを実行し、結果を全て取得する
        Parameters
        ----------
        columns : 実行したいSQL(str)            
        Returns
        ----------
        data: 1行分をタプルとし、複数行をリストとして返す(list)
        """
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        return res
    
    def execute_scalor(self,sql):
        """ 結果の値が1つしかないSQLを実行し、結果を取得する
        Parameters
        ----------
        columns : 実行したいSQL(str)
        Returns
        ----------
        res: 実行結果により返された値
        """
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        conn.close()
        return res[0] if res != None else None
    
    def create(self,tablename,columns,primarykey = '',is_drop=False):
        """ テーブルを作成する
        Parameters
        ----------
        columns : 「列名」又は「列名+型」をカンマ区切りで指定(str)
        primarykey: プライマリーキーをカンマ区切りで指定(str)
        """
        if is_drop :
            self.drop(tablename)
        pkey = ',primary key({0})'.format(primarykey) if primarykey != '' else ''
        sql = 'create table {0}({1} {2})'.format(tablename,columns,pkey)
        self.execute(sql)
   
    def get_column_type(self,tablename):
        """ 指定したテーブルのカラムと型を一覧で取得する
        Parameters
        ----------
        tablename : テーブル名(str)
        Returns
        ----------
        res: リスト形式でカラム名と型のタプルを返す(str)
        """
        res = self.execute_query(self.GET_COLUMN_LIST_QUERY.format(tablename,self.scheme))
        return [(name[1],name[2]) for name in res]
    
    def get_column_list(self,tablename):
        """ 指定したテーブルのカラム名を一覧で取得する
        Parameters
        ----------
        tablename : テーブル名(str)            
        Returns
        ----------
        res: リスト形式のカラム名一覧(str)
        """
        res = self.execute_query(self.GET_COLUMN_LIST_QUERY.format(tablename,self.scheme))
        return [name[1] for name in res]