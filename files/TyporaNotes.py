import os
import threading
import time
NotesDirectoryPath = "E:/Codes/Notes"
TyporaPath = "C:/Program Files/Typora"

anilist = [0,'-','\\','|','/']

class gitpull(threading.Thread):
	def __init__(self) -> None:
		super().__init__()
	def run(self):
		os.system("cd \"%s\" && git pull"%NotesDirectoryPath)


thread1 = gitpull()
thread1.start()
while(thread1.is_alive()):
	print((anilist[anilist[0]+1])+"\r", end="")
	time.sleep(0.1)
	anilist[0] = (anilist[0]+1)%4
print("\rstart Typora", end="")
main = "\"%s/Typora.exe\" %s"%(TyporaPath,NotesDirectoryPath)
os.system(main)
#print("\r        \r", end="")
os.chdir(NotesDirectoryPath)
os.system("git add -u .")
os.system("git add .")
commit = input("Commit here:")
if commit == "":
	t = time.localtime()
	commit = "{:0>2d}/{:0>2d}/{:0>2d}_{:0>2d}:{:0>2d}:{:0>2d}".format(t.tm_year%100, t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)
os.system("git commit -m %s"%commit)
