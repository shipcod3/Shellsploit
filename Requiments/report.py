#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import random
import subprocess 
import urllib
import re
import sys
import os
import time
import platform
import ctypes

def reporter( reportinfo):
	#2F-[Future Features Beta] 
	#For a while I'm working on 'REPORT' system, for help shellsploit users.
	#If you need help, please sent us report logs.
	#This is will be part of shellsploit project ..
	filenname = str(random.randint(99999,99999999))+".txt"
	with open(filenname,"w") as report:
		reportinfo = """
//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//%s - %s

//Python version: %s
//Platform: %s
//Machine: %s

%s
		"""  % (time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"),
			    sys.version.split('\n')[0],platform.machine(),platform.platform(),
				logs)
		print "\n\tLogs are saved : %s\n" % (os.getcwd()+os.sep+filename) 
		report.write(reportinfo)
		report.close()

