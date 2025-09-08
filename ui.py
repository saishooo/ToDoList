import tkinter as ui
from main import main_function
from main import TskData
import csv
import os

g_tsk_management=[]   #グローバル変数

#csvファイルをリスト化して読み込む
def load_csv_data():
    global g_tsk_management   #グローバル変数tsk_management
    if os.path.exists("data.csv"):
        with open("data.csv","r",encoding="utf-8") as f:
            datalist=csv.reader(f)          #csvファイルからデータを取り出して、datalistに格納する
            g_tsk_management=list(datalist)   #tsk_managementにdata.csvのデータをlistにして格納する

#入力内容を読み出し
def get_values():
    values_tsk=str(input_tsk.get()) #タスクを取り出して格納
    values_day=input_day.get()      #期日データを取り出して格納
    values_juge=False               #タスク未実行の状態
    global g_tsk_management
    tsk_data_add=TskData(values_tsk,values_day,values_juge)
    main_function(tsk_data_add)
    load_csv_data()
    update_listbox()

#リストボックスに表示する
def update_listbox():
    global g_tsk_management
    listbox_tsk_now.delete(0,ui.END)    #リストボックス内を削除する
    for t in g_tsk_management:
        listbox_tsk_now.insert(ui.END,f"{t[0]} {t[1]}") #リストボックスにタスクと期日を追加する


root=ui.Tk()
root.title(u"ToDoリスト")
root.geometry("500x500")

load_csv_data() #tsk_managementにcsvファイル内のものをリスト化して入れる。

#タスク追加入力フォーム
label_tsk=ui.Label(root,text="タスク")
label_tsk.pack(anchor="w",padx=5)

input_tsk=ui.Entry(root,width=20)
input_tsk.pack(anchor="w",padx=5)

#タスク期日入力フォーム
label_day=ui.Label(root,text="期日(XXXX-YY-ZZ)")
label_day.pack(anchor="w",padx=5)

input_day=ui.Entry(root,width=20)
input_day.pack(anchor="w",padx=5)

#タスク追加ボタン
button_add=ui.Button(root,text="タスクの追加",command=get_values)
button_add.pack(anchor="w",padx=5)

#(進行中)タスクを表示する箱
listbox_tsk_now=ui.Listbox(root,width=50,selectmode=ui.SINGLE)
listbox_tsk_now.pack(anchor="w",padx=5)

button_juge=ui.Button(root,text="完了/未完了")
button_juge.pack(anchor="w",padx=5)

button_dele=ui.Button(root,text="削除")
button_dele.pack(anchor="w",padx=5)

update_listbox()

root.mainloop()
