import tkinter
from tkinter import Label, Button, StringVar, messagebox, simpledialog
from tkinter.messagebox import *
import subprocess
import os
import time


MGR_FILE = "manage.py"
MGR_DIR = "webserver_pjt"
MGR_PATH = os.path.join(MGR_DIR, MGR_FILE)


root = tkinter.Tk()
setWidth, setHeight = root.maxsize()
root.geometry('320x210+%d+%d' % ((setWidth-320)/2, (setHeight)/2-210))
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
		if askyesno('操作提示', '是否停止服务？', default='no'):
			button1['text'] = "运行"
			button1['background'] = "#EBEDEF"


def run_mgrshell(run_tp):
	mark = time.strftime("RA+%Y%m%d %H:%M:%S", time.localtime())
	cmd = 'start run_assistant.bat "%s" %s' % (mark, run_tp)
	_bat = subprocess.Popen(cmd, shell=True)
	print()
	button1.config(state=tkinter.DISABLED)
	button2.config(state=tkinter.DISABLED)
	button3.config(state=tkinter.DISABLED)
	root.update()
	_bat.wait()
	while True:
		task_info = subprocess.Popen('tasklist /V | findstr /C:"%s"' % mark, shell=True, stdout=subprocess.PIPE)
		if not task_info.stdout.read():
		    button1.config(state=tkinter.ACTIVE)
		    button2.config(state=tkinter.ACTIVE)
		    button3.config(state=tkinter.ACTIVE)
		    break


def open_explo(url):
	subprocess.run('chrome %s' % url)


label1 = Label(text='web服务',width=25,borderwidth=2,relief='groove',background='#f60',foreground='white')
button1 = Button(text='运行',background="#EBEDEF",command=change_text)
label1.grid(row=0,column=0,columnspan=5,padx=15,pady=10,ipadx=5,ipady=6)
button1.grid(row=0,column=5,padx=30,pady=10,ipadx=5,ipady=2)

label2 = Label(text='管理终端',width=25,borderwidth=2,relief='groove',background='#f60',foreground='white')
button2 = Button(text='运行',background='#EBEDEF',command=lambda:run_mgrshell('python manage.py shell'))
label2.grid(row=1,column=0,columnspan=5,padx=15,pady=10,ipadx=5,ipady=6)
button2.grid(row=1,column=5,padx=30,pady=10,ipadx=5,ipady=2)

label3 = Label(text='数据库终端',width=25,borderwidth=2,relief='groove',background='#f60',foreground='white')
button3 = Button(text='运行',background="#EBEDEF",command=lambda:run_mgrshell('python manage.py dbshell'))
label3.grid(row=3,column=0,columnspan=5,padx=15,pady=10,ipadx=5,ipady=6)
button3.grid(row=3,column=5,padx=30,pady=10,ipadx=5,ipady=2)

button_index = Button(text='首页',command=lambda:open_explo('127.0.0.1:8000/index'))
button_index.grid(row=4,column=3,padx=10,ipadx=5,ipady=2)
button_admin = Button(text='控制台',command=lambda:open_explo('127.0.0.1:8000/admin'))
button_admin.grid(row=4,column=4,ipady=2)


if __name__ == '__main__':
	root.mainloop()