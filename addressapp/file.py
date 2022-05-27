import csv
import os
from message import Messages
from judg import Judgement
from person import Person


class File:
    """ ファイル機能 """
    FILE_NAME = 'addressapp.csv'
    read_list = []
    judg = Judgement()
    try:
        file = os.path.join(os.path.dirname(__file__), FILE_NAME)
        f = open(file, 'a+', encoding='UTF-8')
    except Exception:
        print(Messages.FILE_NOT_OPEN)
        exit()

    def read(self, person_list):
        """ ファイルを開いて読み込み、person_list に追加する
        ファイルの内容が[name, tel]の形に合わない場合は例外処理を行う
        """
        reader = csv.reader(self.f)
        self.f.seek(0)
        for line in reader:
            # 重複する行が出てきた場合
            if line in self.read_list:
                self.close()
                raise Exception(Messages.FAILED_READ_FILE)
            self.read_list.append(line)
        for line in self.read_list:
            # ファイルの内容が形式に合わない場合
            if len(line) == 2:
                if self.judg.name_check(line[0])\
                    and self.judg.tel_check(line[1]):
                    p = Person()
                    p.set_name = line[0]
                    p.set_tel = line[1]
                    person_list.append(p)
                else:
                    raise Exception(Messages.FAILED_READ_FILE)
            else:
                raise Exception(Messages.FAILED_READ_FILE)

    def write(self, person_list):
        """ ファイルの初期化をして、person_listをファイルに書き込む """
        self.f.truncate(0)
        writer = csv.writer(self.f, lineterminator='\n')
        for person in person_list:
            writer.writerow([person.name, person.tel])

    def close(self):
        """ クラス内のf を閉じる """
        self.f.close()
