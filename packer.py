import subprocess
import os

def command(cmd):
	process = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
	output, error = process.communicate()

	outputClean = output.splitlines()
	for t in outputClean:
		print(t)
	return outputClean

def checkFolders(folders):
	for fld in folders:
		if not os.path.exists(fld+"/"):
			try:
				os.mkdir(fld)
				print("Created folder! "+fld)
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
				pass

print("=======[Starting]======")
print("Checking folders...")
folder = []
folder.append("in")
folder.append("in/n")
folder.append("in/e")
folder.append("in/w")
folder.append("in/s")
folder.append("out")
checkFolders(folder)
print("Folder check finised...")

directories = ['n','s','e','w']
res = command("ls in/")
print(res)
for r in res:
	r = r.decode("UTF-8")
	if r in directories:
		print("Calling java for "+r)
		command("java -jar runnable-texturepacker.jar in/"+r+"/ out/"+" "+r+" pack.json")
print("======[Finished]======")	