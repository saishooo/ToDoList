import ui
import json

class TskData:
    def __init__(self,tsk,day,juge):
        self.tsk=tsk
        self.day=day
        self.juge=juge

#main処理
def main_function(tskdata):
    write_json(tskdata.tsk,tskdata.day,tskdata.juge)


#ファイルの読み込み
def write_json(a,b,c):
    with open("data.json", mode="a") as json_file:
        json_file.writelines(f"{a},{b},{c}")
