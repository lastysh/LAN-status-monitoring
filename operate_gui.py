import tkinter
from tkinter import Label, Button, StringVar, messagebox, simpledialog
from tkinter.messagebox import *
import subprocess


root = tkinter.Tk()
# print(dir(root))
setWidth, setHeight = root.maxsize()
root.geometry('320x190+%d+%d' % ((setWidth-320)/2, (setHeight)/2-190))
root.title('运行助手')
root.resizable(width=False, height=False)

bvar1 = StringVar()
bvar1.set('start')


def change_text():
	if button1['text'] != "停止":
		button1['text'] = "停止"
		button1['background'] = "#32A084"
		messagebox.showinfo(title='提示信息', message='开始运行')
	else:
		if askyesno("操作提示", "是否停止服务？", default="no"):
			button1['text'] = "运行"
			button1['background'] = "#EBEDEF"





# print(dir(bvar1))
label1 = Label(text='web服务',width=25,borderwidth=2,relief="groove",background="#f60",foreground="white")
print(dir(label1))
'''
grid_configure(cnf={}, **kw) method of tkinter.Label instance
    Position a widget in the parent widget in a grid. Use as options:
    column=number - use cell identified with given column (starting with 0)
    columnspan=number - this widget will span several columns
    in=master - use master to contain this widget
    in_=master - see 'in' option description
    ipadx=amount - add internal padding in x direction
    ipady=amount - add internal padding in y direction
    padx=amount - add padding in x direction
    pady=amount - add padding in y direction
    row=number - use cell identified with given row (starting with 0)
    rowspan=number - this widget will span several rows
    sticky=NSEW - if cell is larger on which sides will this
                  widget stick to the cell boundary
'''
button1 = Button(text='运行',background="#EBEDEF",command=change_text)
label1.grid(row=0,column=0,padx=15,pady=10,ipadx=5,ipady=6)
button1.grid(row=0,column=5,padx=30,pady=10,ipadx=5,ipady=2)

label2 = Label(text='管理终端',width=25,borderwidth=2,relief="groove",background="#f60",foreground="white")
button2 = Button(text='运行',background="#EBEDEF")
label2.grid(row=1,column=0,padx=15,pady=10,ipadx=5,ipady=6)
button2.grid(row=1,column=5,padx=30,pady=10,ipadx=5,ipady=2)

label3 = Label(text='数据库终端',width=25,borderwidth=2,relief="groove",background="#f60",foreground="white")
button3 = Button(text='运行',background="#EBEDEF")
label3.grid(row=3,column=0,padx=15,pady=10,ipadx=5,ipady=6)
button3.grid(row=3,column=5,padx=30,pady=10,ipadx=5,ipady=2)

# bottom_button1 = Button(text='口令1')
# bottom_button1.grid(row=4, column=0)
# bottom_button2 = Button(text='口令1')
# bottom_button2.grid(row=4, column=1)
# bottom_button3 = Button(text='口令1')
# bottom_button3.grid(row=4, column=2)

if __name__ == '__main__':
	root.mainloop()