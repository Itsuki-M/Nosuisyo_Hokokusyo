import os
from tkinter import messagebox
import tkinter.filedialog

def button1_clicked(btn_value, now_date):
  folderName = now_date
  iDir = os.path.abspath(os.path.dirname(__file__))
  nowPath = tkinter.filedialog.askdirectory(initialdir=iDir)
  
  if btn_value == "A" or btn_value == "C":
    folderPath = os.path.join(nowPath, '野菜', folderName)
  elif btn_value == "B":
    folderPath = os.path.join(nowPath, '基礎', folderName)
  elif btn_value == "D":
    folderPath = os.path.join(nowPath, '加工食品', folderName)
  
  folders = ['1.北海道', '2.東北', '3.関東','4.北陸', '5.東海', '6.近畿', '7.中四国', '8.九州', '9.沖縄']
  
  if not os.path.exists(folderPath):
    os.makedirs(folderPath)
    for folder in folders:
      os.makedirs(os.path.join(folderPath, folder))
    messagebox.showinfo('成功', '今週のフォルダを作成しました')
  else:
    messagebox.showinfo('失敗', '既にフォルダが存在します')