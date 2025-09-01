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
    i=7 #タスク進行の最終行
    z=read_load_now(i)

#未達成なタスクを表示する関数
def read_load_now(a):
    with open("data.csv",mode="r") as read_csv:
        dataread=csv.reader(read_csv)   #csvファイルの読み出し
        rows=list(dataread)     #csvファイル内のデータをリスト化
        #出力
        if not rows:    #リスト内がからの場合は実行しない
             return 0
        else:   #リストが空でなければ実行する
            for s in rows:
                if(s[2]=="0"):  #実行済みのものは表示しない
                    for j in range(3):
                            label_tsk_csv=ui.Label(root,text=s[j])
                            label_tsk_csv.grid(row=a,column=j)
                a+=1


root=ui.Tk()
root.title(u"ToDoリスト")
root.geometry("500x500")
i=0

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

#進行中タスク表示ラベル
label_tsk_now=ui.Label(root,text="進行中タスク")
label_tsk_now.grid(row=i,column=0)
label_day_now=ui.Label(root,text="期日")
label_day_now.grid(row=i,column=1)
label_juge_now=ui.Label(root,text="完了")
label_juge_now.grid(row=i,column=2)
i+=1

#未達成タスク表示
i=read_load_now(i)

root.mainloop()
