import subprocess
import os

repo = raw_input("Name of REPO: ")
user = raw_input("Username: ")

subprocess.call(["mkdir", "neut"])
os.chdir("neut")

subprocess.call(["git", "clone", "https://github.com/"+user+"/"+repo])

os.chdir(repo)
#algorithm to find all gendered pronouns using gender dictionary
#http://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
for subdir, dirs, files in os.walk("/"+repo):
    for file in files:
    	filepath = subdir + os.sep + file
    	#http://stackoverflow.com/questions/11678939/replace-text-based-on-a-dictionary
        subprocess.call(["awk","-f","foo.awk","dict.dat",filepath])

#if nothings changed, be done
if subprocess.call(["git","status"]):
	print 'stuff'

subprocess.call(["git","add","-A"])

subprocess.call(["git","commit","-m","Deleted gendered pronouns and replaced with more appropriate gender neutral versions."])

subprocess.call(["git","push","origin","master"])
 
#subprocess.call(["rm","-rf","/tmp/"+repo])
