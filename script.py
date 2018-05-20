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
folder.append("out")
checkFolders(folder)
directories = ['n','s','e','w']
res = command("ls in/")
for r in res:
	if r in directories:
		command("java -jar runnable-texturepacker.jar in/"+r+"/ out/"+" "+r+" pack.json")
print("======[Finished]======")