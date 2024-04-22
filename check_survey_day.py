from tkinter import messagebox
def check_survey_day(pre_week,this_week,btn_value):
  if pre_week == "" or this_week == "":
    messagebox.showinfo('エラー', '調査年月日を入力してください')
    return False
  elif btn_value == "A":
    if len(pre_week) != 6 or len(this_week) != 6:
      messagebox.showinfo('エラー', '調査年月日の桁数が正しくありません。')
      return False
  elif btn_value == "B":
    if len(pre_week) != 6 or len(this_week) != 4:
      messagebox.showinfo('エラー', '調査年月日の桁数が正しくありません。')
      return False
  elif btn_value == "C":
    if len(pre_week) != 4 or len(this_week) != 6:
      messagebox.showinfo('エラー', '調査年月日の桁数が正しくありません。')
      return False
  elif btn_value == "D":
    if len(pre_week) != 4 or len(this_week) != 4:
      messagebox.showinfo('エラー', '調査年月日の桁数が正しくありません。')
      return False