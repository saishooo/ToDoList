import tkinter as ui
import csv
import os

g_tsk_management=[]   #グローバル変数

#クラスの宣言
class TskData:
    def __init__(self,tsk,day,juge):
        self.data=[tsk,day,juge]

#csvファイルをリスト化して読み込む
def load_csv_data():
    global g_tsk_management                     #グローバル変数tsk_management
    if os.path.exists("data.csv"):
        with open("data.csv","r",encoding="utf-8") as f:
            datalist=csv.reader(f)              #csvファイルからデータを取り出して、datalistに格納する
            g_tsk_management=list(datalist)     #tsk_managementにdata.csvのデータをlistにして格納する

#data.csvファイルに保存する
def save_tsks():
     global g_tsk_management
     with open("data.csv", mode="w") as write_csv_file:
        for t in g_tsk_management:
            write_csv_file.writelines(f"{t[0]},{t[1]},{t[2]}\n")

#リストボックスに表示する
def update_listbox():
    global g_tsk_management
    listbox_tsk_now.delete(0,ui.END)                            #リストボックス内を削除する
    for t in g_tsk_management:
        listbox_tsk_now.insert(ui.END,f"{t[0]} {t[1]} {t[2]}")  #リストボックスにタスクと期日を追加する
    save_tsks()

#入力内容を読み出し
def get_values():
    global g_tsk_management
    values_tsk=str(input_tsk.get()) #タスクを取り出して格納
    values_day=input_day.get()      #期日データを取り出して格納
    values_juge=False               #タスク未実行の状態
    tsk_data_add=TskData(values_tsk,values_day,values_juge)
    g_tsk_management.append(tsk_data_add.data)
    save_tsks()
    update_listbox()
    load_csv_data()

#タスクを削除する
def tsk_del():
    index=listbox_tsk_now.curselection()
    global g_tsk_management
    if index:
        del g_tsk_management[index[0]]
        update_listbox()

#完了未完了の切り替えを行う関数 
def tsk_juge():
    index=listbox_tsk_now.curselection()    #listboxで選択されている項目を取得
    global g_tsk_management
    if not index:
        return
    
    if g_tsk_management[index[0]][2]==False:
        g_tsk_management[index[0]][2]=True
        update_listbox()
    else:
        g_tsk_management[index[0]][2]=False
        update_listbox()


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

button_juge=ui.Button(root,text="完了/未完了",command=tsk_juge)
button_juge.pack(anchor="w",padx=5)

button_dele=ui.Button(root,text="削除",command=tsk_del)
button_dele.pack(anchor="w",padx=5)

update_listbox()

root.mainloop()
