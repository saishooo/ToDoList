import tkinter as ui
from main import main_function
from main import TskData
import csv


#入力内容を読み出し処理
def get_values():
    values_tsk=str(input_tsk.get())
    values_day=input_day.get()
    values_juge=0       #タスク未実行の状態
    tsk_management=[]
    tsk_management=TskData(values_tsk,values_day,values_juge)
    main_function(tsk_management)

root=ui.Tk()
root.title(u"ToDoリスト")
root.geometry("500x500")

#進行中タスク表示ラベル
i=0
label_tsk_now=ui.Label(root,text="進行中タスク")
label_tsk_now.grid(row=i,column=0)
label_tsk_now=ui.Label(root,text="期日")
label_tsk_now.grid(row=i,column=1)
label_tsk_now=ui.Label(root,text="完了")
label_tsk_now.grid(row=i,column=2)
i+=1

#進行中タスク表示
with open("data.csv",mode="r") as read_csv:
    dataread=csv.reader(read_csv)   #csvファイルの読み出し
    rows=list(dataread)     #csvファイル内のデータをリスト化
    #出力s
    for s in rows:
        #完了列に1があったら除外する処理はここに追加
        for j in range(3):
            label_tsk_csv=ui.Label(root,text=s[j])
            label_tsk_csv.grid(row=i,column=j)
        i+=1

#タスク追加入力フォーム
label_tsk=ui.Label(root,text="タスク")
label_tsk.grid(row=i,column=0)
input_tsk=entry_tsk=ui.Entry(root,width=20)
entry_tsk.grid(row=i,column=1)
i+=1

#タスク日付入力フォーム
label_day=ui.Label(root,text="日付")
label_day.grid(row=i,column=0)
input_day=entry_day=ui.Entry(root,width=20)
entry_day.grid(row=i,column=1)
i+=1

#タスク追加ボタン
button_add=ui.Button(root,text="タスクの追加",command=get_values)
button_add.grid(row=i,column=0)
i+=1

#タスク完了ボタン
button_comp=ui.Button(root,text="タスクの完了")
button_comp.grid(row=i+1,column=0)
i+=1

#タスク削除ボタン
button_del=ui.Button(root,text="タスクの削除")
button_del.grid(row=i+1,column=0)
i+=1

root.mainloop()
