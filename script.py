import subprocess

def command(cmd):
	process = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
	output, error = process.communicate()

	outputClean = output.splitlines()
	for t in outputClean:
		print(t)
	return outputClean


print("=======[Starting]======")
directories = ['n','s','e','w']
res = command("ls in/")
for r in res:
	if r in directories:
		command("java -jar runnable-texturepacker.jar in/"+r+"/ out/"+" "+r+" pack.json")
print("======[Finished]======")