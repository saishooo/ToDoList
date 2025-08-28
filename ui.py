import tkinter as ui
from main import main_function
from main import TskData

#入力内容を読み出し処理
def get_values():
    values_tsk=str(input_tsk.get())
    values_day=input_day.get()
    values_juge=0       #タスク未実行の状態
    tsk_management=TskData(values_tsk,values_day,values_juge)
    main_function(tsk_management)


root=ui.Tk()
root.title(u"ToDoリスト")
root.geometry("500x500")

label_tsk=ui.Label(root,text="タスク")
label_tsk.grid(row=0,column=0)

label_day=ui.Label(root,text="日付")
label_day.grid(row=1,column=0)

input_tsk=entry_tsk=ui.Entry(root,width=20)
entry_tsk.grid(row=0,column=1)

input_day=entry_day=ui.Entry(root,width=20)
entry_day.grid(row=1,column=1)

button_add=ui.Button(root,text="タスクの追加",command=get_values)
button_add.grid(row=3,column=0)

button_comp=ui.Button(root,text="タスクの完了")
button_comp.grid(row=4,column=0)

button_del=ui.Button(root,text="タスクの削除")
button_del.grid(row=5,column=0)

root.mainloop()
