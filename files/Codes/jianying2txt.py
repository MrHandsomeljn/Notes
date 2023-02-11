import sys
openfile = "./files/Codes/jianying2txtInput.txt"
if(len(sys.argv) > 1):
	openfile = sys.argv[1]
includeTime = False
def main():
	inputTexts = []
	import json as JSON
	with open(openfile,"r",encoding="utf-8") as f:
		inputTexts = f.readlines()
	inputText = ""
	for x in inputTexts:
		inputText += x
	jyjson = JSON.loads(inputText)
	temp = jyjson["materials"]["texts"]
	texts = {}
	for x in temp:
		xstr = x["content"].split("[")[1].split("]")[0]
		texts[x["id"]] = xstr
	if(includeTime):
		tracks = jyjson["tracks"]
		for track in tracks:
			segments = track["segments"]
			for segment in segments:
				start = segment["target_timerange"]["start"]
				end = start + segment["target_timerange"]["duration"]
				try: print(time2Text(start)+"-->"+time2Text(end)+": "+texts[segment["material_id"]])
				except:	pass
	else:
		for x in texts.values(): print(x)
def time2Text(time):
	time //= 1000
	millisecond = time % 1000
	time = time // 1000
	second = time % 60
	time = time // 60
	minute = time % 60
	time = time // 60
	hour = time
	return str.format("{:02d}:{:02d}:{:02d},{:03d}",hour,minute,second,millisecond)
if __name__ == "__main__":
	ch = input("是否需要时间？ Y/[N]")
	if(ch.__len__() > 0 and (ch[0] == 'y' or ch[0] == 'Y')) : includeTime = True
	main()