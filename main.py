import ui
import csv

class TskData:
    def __init__(self,tsk,day,juge):
        self.tsk=tsk
        self.day=day
        self.juge=juge

#main処理
def main_function(tskdata):
    write_csv(tskdata.tsk,tskdata.day,tskdata.juge)


#ファイルの読み込み
def write_csv(a,b,c):
    with open("data.csv", mode="a") as write_csv_file:
        write_csv_file.writelines(f"{a},{b},{c}\n")
