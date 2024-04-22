from tkinter import *
from tkinter import ttk
from button1_clicked import button1_clicked
from button2_clicked import button2_clicked

root = Tk()
root.title("報告書作成ツール")
root.geometry("470x230")

frame1 = ttk.Frame(root, padding=10)

label_frame1 = ttk.LabelFrame(frame1, text="作成物選択", padding=(10))
v1 = StringVar()
rb1 = ttk.Radiobutton(label_frame1, text="野菜→野菜", value="A", variable=v1)
rb2 = ttk.Radiobutton(label_frame1, text="野菜→基礎", value="B", variable=v1)
rb3 = ttk.Radiobutton(label_frame1, text="基礎→野菜", value="C", variable=v1)
rb4 = ttk.Radiobutton(label_frame1, text="加工食品→加工食品", value="D", variable=v1)

label_frame2 = ttk.LabelFrame(frame1, padding=(10))
label1 = ttk.Label(label_frame2, text="前週調査年月日")
txtbox1 = ttk.Entry(label_frame2, width=10)
label2 = ttk.Label(label_frame2, text="今週調査年月日")
txtbox2 = ttk.Entry(label_frame2,width=10)

label_frame3 = ttk.LabelFrame(frame1, padding=(10))
button1 = ttk.Button(label_frame3, text="フォルダ作成", command=lambda: button1_clicked(v1.get(), txtbox2.get()))
button2 = ttk.Button(label_frame3, text="報告書作成", command=lambda: button2_clicked(v1.get(), txtbox1.get(), txtbox2.get()))

frame1.grid()
label_frame1.grid(row=0, column=0)
rb1.grid(row=0, column=0, padx=5)
rb2.grid(row=0, column=1, padx=5)
rb3.grid(row=0, column=2, padx=5)
rb4.grid(row=0, column=3, padx=5)

label_frame2.grid(row=1, column=0)
label1.grid(row=1, column=0),
txtbox1.grid(row=1, column=1)
label2.grid(row=1, column=2)
txtbox2.grid(row=1, column=3)

label_frame3.grid(row=2, column=0)
button1.grid(row=2, column=0, padx=5)
button2.grid(row=2, column=1, padx=5)

root.mainloop()