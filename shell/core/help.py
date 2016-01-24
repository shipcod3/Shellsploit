#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from color import *

def mainhelp():
	print bcolors.GREEN+"""
Usage Commands
===============
\tCommands		Description
\t------------		-------------
\thelp           		Help menu
\tos			Command directly ur computer
\tuse 			Select Module For Use
\tclear			Clear the menu
\tshow modules    	Show Modules of Current Database
\tshow backdoors    	Show Backdoors of Current Database
\tshow injectors		Show Injectors(Shellcode,dll,so etc..)
""" 

def shellcodehelp():
	print bcolors.GREEN+"""
Shellcode Commands
===================
\tCommands		Description
\t------------		-------------
\tback			Exit Current Module
\tset 			Set Value Of Options To Modules
\tip			Get IP address(Requires net connection)
\tos			Command directly ur computer
\tclear			Clear the menu
\tdisas			Disassembly the shellcode(Support : x86/x64)
\twhatisthis      	Learn which kind of shellcode it is
\titeration		Encoder iteration time
\tgenerate 		Generate shellcode 
\toutput 			Save option to shellcode(txt,py,c,cpp,exe)
\tshow encoders		List all obfucscation encoders
\tshow options		Show Current Options Of Selected Module
""" 
	
def injectorhelp():
	print bcolors.GREEN+"""
Injector  Commands
===================
	Commands		Description
	------------	\t-------------
	set 			Set Value Of Options To Modules
	help 			Help menu
	back			Exit Current Module
	os  			Command directly ur computer
	pids			Get PID list of computer
	getpid			Get specific PID on list(Ex. getpid Python)
"""	