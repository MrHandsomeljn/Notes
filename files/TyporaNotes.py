import os
import threading
import time
import tkinter as tk
import tkinter.messagebox

from click import command
NotesDirectoryPath = "E:/Codes/Notes"
TyporaPath = "C:/Program Files/Typora"

anilist = [0,'-','\\','|','/']

class gitpull(threading.Thread):
	def __init__(self) -> None:
		super().__init__()
	def run(self):
		os.system("cd \"%s\" && git pull"%NotesDirectoryPath)

root = tk.Tk()
root.minsize(500,500)
root.resizable(0,0)
root.withdraw()

needPull = tkinter.messagebox.askokcancel('Git', 'sync from Github repository?')
if needPull:
	thread1 = gitpull()
	thread1.start()
	while(thread1.is_alive()):
		print((anilist[anilist[0]+1])+"\r", end="")
		time.sleep(0.1)
		anilist[0] = (anilist[0]+1)%4
print("\rstart Typora", end="")
main = "\"%s/Typora.exe\" %s"%(TyporaPath,NotesDirectoryPath)
os.system(main)
os.chdir(NotesDirectoryPath)
os.system("git add -u .")
os.system("git add .")

needCommit, commit = False, ""
class getcommit(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title("Commit")
		self.setupUI()
	
	def setupUI(self):
		row1 = tk.Frame(self)
		row1.pack(fill="x")
		l1 = tk.Label(row1, text="Commit here:",height=2,width=10)
		l1.pack(side=tk.LEFT)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
		self.xls_text = tk.StringVar()
		ent1 = tk.Entry(row1, textvariable=self.xls_text)
		ent1.pack(side=tk.RIGHT)
		ent1.bind("<Return>", self.submit)
		row2 = tk.Frame(self)
		row2.pack(fill="x")
		tk.Button(row2, text="确认", command=self.on_click_yes).pack(side=tk.LEFT)
		tk.Button(row2, text="取消", command=self.on_click_no).pack(side=tk.RIGHT)

		pass

	def on_click_yes(self):
		global needCommit, commit
		needCommit, commit = True, self.xls_text.get().lstrip()
		self.quit()
		self.destroy()
	
	def on_click_no(self):
		global needCommit, commit
		needCommit, commit = False, ""
		self.quit()
		self.destroy()
	
	def submit(self, ev = None):
		self.on_click_yes()

app = getcommit()
app.wm_attributes('-topmost',1)
app.mainloop()

if needCommit:
	if commit == "":
		t = time.localtime()
		commit = "{:0>2d}/{:0>2d}/{:0>2d}_{:0>2d}:{:0>2d}:{:0>2d}".format(t.tm_year%100, t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)
	os.system("git commit -m %s"%commit)

	print("###### git push ######")
	os.system("git push")