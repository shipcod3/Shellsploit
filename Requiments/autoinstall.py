#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from report import *


def download( ):
	#Windows
	db = urllib.urlopen("https://pypi.python.org/pypi/setuptools#downloads").read()
	find = re.findall("https://pypi.python.org/packages/source/s/setuptools/\S+#", db)
	find = str(find[1]).replace("#", "")
	filename = find.split("/")[-1]
	foldername = filename.replace(".zip", "")


	try:
		urllib.urlretrieve(find, os.getcwd()+os.sep+filename)
		print "File download complate : %s " % filename
		import zipfile
		#https://docs.python.org/2/library/zipfile.html

		with zipfile.ZipFile(filename) as myzip:				
			myzip.extractall(os.getcwd()+os.sep+foldername)
			myzip.close()
		finalcommand = "python "+foldername+os.sep+foldername+os.sep+"setup.py install"

	except Exception as error:
		print "Unexpected error while download : %s " % error
		sys.exit()  

	db = subprocess.Popen(finalcommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
	db = db.stdout.read()

	if "Finished processing dependencies for" in db:
		for x in [filename,foldername]:
			try:
				os.remove(x)
			except:
				pass
		Windows() 
	else:
		print "Unkown error .."
		print "Please install manuel way .."
		print "Page : https://pypi.python.org/pypi/setuptools#downloads"



def Windows():
	#easy_install much better for windows, coz easy_install install dependencies while install target library.
	#And python not coming with python ..
	try:
		#setx command seems like not native command on XP(coz its old)
		#Mentioned here ; http://stackoverflow.com/a/17803827
		#So if you are XP user, like me.You must add ur path manuel until I fix it ..
		subprocess.Popen('setx path "%path%;C:\Python27;C:\Python27\Scripts;"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
		#http://superuser.com/questions/135056/set-permanent-environmental-variable-in-windows-xp 
		#This is looks like working so, I will use it for only XP users lol.But not in BETA ..
	except:
		pass

	db = subprocess.Popen("easy_install", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
	if "error: No urls, filenames, or requirements specified (see --help)" not in db.stdout.read():
		download()
	else:
		install()


def install():
	logs = ""
	commands = [
		"easy_install pyreadline",
		"easy_install distorm3",
		#"easy_install colorama"
	]
	for x in commands:
		db = subprocess.Popen(x, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
		db = db.stdout.read()
		if "Finished processing dependencies for" in db:
			print "Finished install : %s .." % x
		else:
			logs += "%s\n%s\n" % (x,len(x)*"=")
			logs += db+"\n\n"
			print "Failed install : %s .." % x
			
	if logs != "":
		reporter(logs)
	else:
		print "Everything is fine !"
	




def Linux():
	#https://bootstrap.pypa.io/get-pip.py
	#Please check get-pid.py before install for ur safety.
	db = subprocess.Popen("pip --help", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
	if "Usage" not in db.stdout.read():
		path = "python "+os.getcwd+os.sep+"get-pid.py"
		db = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if "Successfully installed" in db.stdout.read():
			print "Everything is fine !"
		else:
			install()


def start():
	#Public way,just edit little bit ..
	try:
		adminrights = os.getuid() == True
	except AttributeError:
		adminrights = ctypes.windll.shell32.IsUserAnAdmin() == True
	else:
		adminrights = False

	if not adminrights:
		sys.exit("This script requires admin privileges to execute ..")
	else:
		oslist = [
			"sunos",
			"freebsd",
			"openbsd",
			"netbsd",
			"linux",
			"linux2",
			"darwin"
		]
		if sys.platform.lower() in oslist:
			Linux()
		elif "win32" in sys.platform:
			Windows()
		else:
			sys.exit("\nUnkown operation system ..\n")
