#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

#Greetz : Kara Ayaz


from color import *

def controlset( choice, argv1="None", argv2="None", argv3="None", argv4="None"):
	argv3 = str(argv3)
	#Standalone Shellcodes
	list = [
	"freebsd_x64/binsh_spawn",
	"linux86/binsh_spawn",
	"linux86/bindash_spawn",
	"linux64/binsh_spawn",
	"linux/binsh_spawn",
	"osx64/binsh_spawn",
	"freebsd_x86/binsh_spawn",
	"linux_arm/binsh_spawn",
	"linux_mips/binsh_spawn",
	"solarisx86/binsh_spawn",
	"osx86/binsh_spawn"]

	#Dependent a file 
	list2 = [ 
	"linux/read",
	"FreeBSDx86/read",
	"linux86/read",
	"solarisx86/read",
	"linux86/chmod",
    "linux64/read",
    "linux_arm/chmod",
	"linux86/mkdir",
	"linux_arm/chmod"]

	list3 = [
	"linux86/tcp_bind",
	"linux/tcp_bind",
	"linux64/tcp_bind",
	"osx86/tcp_bind",
	"osx64/tcp_bind",
	"freebsd_x86/tcp_bind"]

	list4 = [
	"freebsd_x86/reverse_tcp",
	"freebsd_x64/reverse_tcp",
	"freebsd_x86/reverse_tcp2",
	"linux/reverse_tcp",
	"linux86/reverse_tcp",
	"linux64/reverse_tcp",
	"osx64/reverse_tcp",
	"linux_mips/reverse_tcp",
	"osx86/reverse_tcp",
	"solarisx86/reverse_tcp",
	]

	#Execve
	list5 = [
		"linux_arm/exec",
		"freebsd_x86/exec"
		"linux86/exec",
		"windows/exec",
	]


	if len(argv1) >= len(argv2):
		if len(argv1) == 0:
			padd = 8
		elif len(argv1) == 1:
			padd = 8
		elif len(argv1) == 2:
			padd = 8
		else:
			padd = len(argv1)+5
	else:
		padd = len(argv2)+5

	if choice in list:
		print bcolors.GREEN+"""
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tencoder\t\t{3}\t\tno\t\tEncoder type	
\titeration\t{4}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv1.ljust(padd),argv2.ljust(padd))

	elif choice in list2:
		print bcolors.GREEN+"""
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tfile\t\t{3}\t\tyes\t\tFile name&path
\tencoder\t\t{4}\t\tno\t\tEncoder type	
\titeration\t{5}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv1.ljust(padd),argv2.ljust(padd),argv3.ljust(padd))

	elif choice in list3:
		print bcolors.GREEN+"""
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tport\t\t{3}\t\tyes\t\tThe listen port
\tencoder\t\t{4}\t\tno\t\tEncoder type	
\titeration\t{5}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv1.ljust(padd),argv2.ljust(padd),argv3.ljust(padd),argv4.ljust(padd))
	
	elif choice in list4:
		if len(argv2) >= len(argv3):
			if len(argv2) == 0:
				padd = 8
			elif len(argv2) == 1:
				padd = 8
			elif len(argv2) == 2:
				padd = 8
			else:
				padd = len(argv2)+5
		else:
			padd = len(argv3)+5


		info_  = "port"
		info__ = "host\t\t"
		infodesc_  = "Connect PORT"
		infodesc__ = "Connect HOST" 


		print bcolors.GREEN+"""
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\t{3}\t\t{4}\t\tyes\t\t{5}
\t{6}{7}\t\tyes\t\t{8}
\tencoder\t\t{9}\t\tno\t\tEncoder type		
\titeration\t{10}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	info_,argv1.ljust(padd),infodesc_,info__,argv2.ljust(padd),infodesc__,argv3.ljust(padd),argv4.ljust(padd))

	
	elif choice in list5:
		if len(argv3) >= len(argv2):
			if len(argv3) == 0:
				padd = 8
			elif len(argv3) == 1:
				padd = 8
			elif len(argv3) == 2:
				padd = 8
			else:
				padd = len(argv3)+5
		else:
			padd = len(argv2)+5
		
		print bcolors.GREEN+"""
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tcommand\t\t{3}\t\tyes\t\tCommand to execute
\tencoder\t\t{4}\t\tno\t\tEncoder type	
\titeration\t{5}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv3.ljust(padd),argv2.ljust(padd),argv1.ljust(padd))


	else:
		if choice == "windows/messagebox":
			print bcolors.GREEN+"""
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tmessage\t\t%s\t\t\tyes\t\tFile name/path to remove
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv1,argv2,argv3)

		elif choice == "windows/download&execute":
			print bcolors.GREEN+"""
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tlink\t\t%s\t\t\tyes\t\tSource to download exe
	\tfilename\t%s\t\t\tyes\t\tFile name
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv3,argv4,argv2,argv1)


		#Will be change
		elif choice == "freebsd_x64/tcp_bind":
			print bcolors.GREEN+"""
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tpassword\t%s\t\t\tyes\t\tPassword for connection
	\tPORT\t\t%s\t\t\tyes\t\tPort to bind connection
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv4,argv3,argv2,argv1)


