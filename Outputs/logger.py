#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from random import randint
import os

def logs(  data=None, extension=None):
	while True:
		if extension == None:
			name = "%s" % str(randint(0, 999999999))
		else:
			name = "%s.%s" % (str(randint(0, 999999999)),extension)

		if not os.path.isfile(name):
			break

	if extension == None:
		logs = open(name, "wb")
	else:
		logs = open(name, "w")
		
	logs.write(data)
	logs.close()
	if extension != None:
		print "\n\t[+]Script file : %s saved !\n" % (os.getcwd()+os.sep+name)
	else:
		print "\n\t[+]Executable file : %s saved !\n" % (os.getcwd()+os.sep+name)

