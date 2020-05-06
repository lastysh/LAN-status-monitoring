import tkinter
import subprocess
import os
import time
import re
import sys
from tkinter import Label, Button, StringVar, messagebox, simpledialog
from tkinter.messagebox import *


MGR_FILE = "manage.py"
MGR_DIR = "webserver_pjt"
MGR_PATH = os.path.join(MGR_DIR, MGR_FILE)


root = tkinter.Tk()
setWidth, setHeight = root.maxsize()
root.geometry('320x230+%d+%d' % ((setWidth-320)/2, (setHeight)/2-230))
root.title('运行助手')
root.resizable(width=False, height=False)


def open_explo(url):
	subprocess.Popen('chrome %s' % url)


def find_thread():
	td = subprocess.Popen('netstat -ano | findstr "8000"', shell=True, stdout=subprocess.PIPE).stdout.read()
	return td


def kill_task(res:str):
	try:
		pid_value = re.findall(r'LISTENING\s+?(\d+)', res.decode())[0]
	except:
		messagebox.showwarning(title='提示信息', message='Error: 未知错误')
		root.destroy()
		sys.exit(0)
	subprocess.Popen('taskkill /F /pid %s' % pid_value, shell=True, stdout=subprocess.PIPE)


def test_bbtn():
	if bvar1.get()=="停止":
		button_index.config(state=tkinter.ACTIVE)
		button_admin.config(state=tkinter.ACTIVE)
	else:
		button_index.config(state=tkinter.DISABLED)
		button_admin.config(state=tkinter.DISABLED)
	root.update()


def change_text():
	if button1['text'] != "停止":
		run_mgrshell('python manage.py runserver')
		bvar1.set("停止")
		button1['background'] = "#32A084"
		# messagebox.showinfo(title='提示信息', message='开始运行')
		bottom_show['text'] = "开始运行"
		test_bbtn()
		time.sleep(0.5)
		bottom_show['text'] = "服务已启动"
	else:
		if askyesno('操作提示', '是否停止服务？', default='no'):
			search_res = find_thread()
			if search_res:
				kill_task(search_res)
				bvar1.set("运行")
				bottom_show['text'] = "停止服务"
				test_bbtn()
				button1['background'] = "#EBEDEF"
				time.sleep(0.5)
				bottom_show['text'] = "就绪"
			else:
				bottom_show['text'] = "未就绪"
				messagebox.showwarning(title='提示信息', message='服务进程不存在！')
				bvar1.set("运行")
				bottom_show['text'] = "就绪"
				test_bbtn()
				button1['background'] = "#EBEDEF"


def run_mgrshell(run_tp):
	mark = time.strftime("RA+%Y%m%d %H:%M:%S", time.localtime())
	cmd = 'start run_assistant.bat "%s" %s' % (mark, run_tp)
	_bat = subprocess.Popen(cmd, shell=True)
	# button1.config(state=tkinter.DISABLED)
	# button2.config(state=tkinter.DISABLED)
	# button3.config(state=tkinter.DISABLED)
	# root.update()
	if run_tp == "python manage.py runserver":
		return mark
	root.withdraw()
	_bat.wait()
	while True:
		task_info = subprocess.Popen('tasklist /V | findstr /C:"%s"' % mark, shell=True, stdout=subprocess.PIPE)
		if not task_info.stdout.read():
			# button1.config(state=tkinter.ACTIVE)
			# button2.config(state=tkinter.ACTIVE)
			# button3.config(state=tkinter.ACTIVE)
			root.deiconify()
			break


bvar1 = StringVar()
bvar1.set('运行')

label1 = Label(text='web服务',width=25,borderwidth=2,relief='groove',background='#f60',foreground='white')
button1 = Button(textvariable=bvar1,background="#EBEDEF",command=change_text)
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

bottom_show = Label(foreground='blue',width=36,anchor='w')
bottom_show.grid(row=5,column=0,columnspan=6,padx=15,ipadx=5,ipady=6,sticky='W')

ifSetup = find_thread()
test_bbtn()
if ifSetup:
	root.withdraw()
	if messagebox.askyesno(title='提示信息', message='8000 端口已被占用，是否帮您停止对应服务？'):
		kill_task(ifSetup)
		bottom_show['text'] = "就绪"
	else:
		button1.config(state=tkinter.DISABLED)
		bottom_show['text'] = "未就绪"
	root.deiconify()


if __name__ == '__main__':
	root.mainloop()