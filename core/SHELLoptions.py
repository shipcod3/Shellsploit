#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


#Greetz : Kara Ayaz


def controlset( choice, argv1="None", argv2="None", argv3="None", argv4="None"):
	argv3 = str(argv3)
	#Standalone Shellcodes
	list = [
	"freebsd_x86/killall",
	"freebsd_x64/binsh_spawn",
	"linux86/egghunter",
	"linux86/binsh_spawn",
	"linux86/bindash_spawn",
	"linux86/reboot",
	"linux86/shutdown",
	"linux86/killall",
	"linux64/binsh_spawn",
	"linux64/shutdown",
	"linux64/reboot",
	"osx64/binsh_spawn",
	"freebsd_x86/reboot",
	"freebsd_x86/binsh_spawn",
	"linux_arm/killall",
	"linux_arm/binsh_spawn",
	"linux_mips/binsh_spawn",
	"linux_mips/reboot",
	"solarisx86/binsh_spawn",
	"solarisx86/killall",
	"solarisx86/egghunter",
	"solarisx86/bindash_spawn",
	"solarisx86/reboot",
	"solarisx86/shutdown",
	"osx86/binsh_spawn"]

	#Dependent a file 
	list2 = [ 
	"freebsd_x86/exec", #Will be change here, we should make different list for exec's
	"FreeBSDx86/read",
	"linux86/readfile",
	"linux86/chmod",
	"linux64/mkdir",
	"linux86/mkdir",
	"linux86/rmdir",
    "linux64/read",
	"linux_arm/creat",
    "linux_arm/chmod",
	"linux86/mkdir",
	"linux_arm/chmod"]

	list3 = [
	"linux86/netcatbind",
	"linux86/tcp_bind",
	"linux64/tcp_bind",
	"osx86/tcp_bind",
	"osx64/tcp_bind",
	"freebsd_x86/tcp_bind",
	"linux86/download&exec"]

	list4 = [
	"freebsd_x86/reverse_tcp",
	"freebsd_x86/netcatreverse",
	"freebsd_x86/reverse_tcp2",
	"linux86/reverse_tcp",
	"linux64/reverse_tcp",
	"osx64/reverse_tcp",
	"linux_mips/reverse_tcp",
	"linux86/reverse_telnet",
	
	"windows/add_user",
	"freebsd_x86/add_user",
	"linux_arm/add_user"]


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
		print """
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tencoder\t\t{3}\t\tno\t\tEncoder type	
\titeration\t{4}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv1.ljust(padd),argv2.ljust(padd))

	elif choice in list2:
		print """
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tfile\t\t{3}\t\tyes\t\tFile name&path
\tencoder\t\t{4}\t\tno\t\tEncoder type	
\titeration\t{5}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	argv1.ljust(padd),argv2.ljust(padd),argv3.ljust(padd))

	elif choice in list3:
		print """
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

		#needle work on strings lol ..
		if choice in ["windows/add_user","freebsd_x86/add_user","linux_arm/add_user"]:
			info_  = "user"
			info__ = "password\t"
			infodesc_  = "Username"
			infodesc__ = "Password" 

		else:
			info_  = "port"
			info__ = "host\t\t"
			infodesc_  = "Connect PORT"
			infodesc__ = "Connect HOST" 


		print """
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\t{3}\t\t{4}\t\tyes\t\t{5}
\t{6}{7}\t\tyes\t\t{8}
\tencoder\t\t{9}\t\tno\t\tEncoder type		
\titeration\t{10}\t\tno\t\tIteration times
""".format(choice,"Current Setting".ljust(padd),"---------------".ljust(padd),
	info_,argv1.ljust(padd),infodesc_,info__,argv2.ljust(padd),infodesc__,argv3.ljust(padd),argv4.ljust(padd))

	

	else:
		#THAT TABLE MUST BE CHANGE ..
		if choice == "windows/exec":
			print """
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tcommand\t\t%s\t\t\tyes\t\tCommand to execute
	\tencoder\t\t%s\t\t\tno\t\tEncoder type	
	\titeration\t%s\t\t\tno\t\tEncoder iteration time
	""" %  (choice,argv3,argv2,argv1)


		elif choice == "linux64/add_map":
			print """
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tip\t\t%s\t\t\tyes\t\tIP to forward
	\tmap\t\t%s\t\t\tyes\t\tHost name to map
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv1,argv2,argv4,argv3)


		elif choice == "windows/messagebox":
			print """
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tmessage\t\t%s\t\t\tyes\t\tFile name/path to remove
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv1,argv2,argv3)

		elif choice == "windows/download&execute":
			print """
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tlink\t\t%s\t\t\tyes\t\tFile name/path to remove
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv1,argv2,argv3)


		#Will be change
		elif choice == "freebsd_x64/tcp_bind":
			print """
	Module options (%s):

	\tName\t\tCurrent Setting\t\tRequired\tDescription
	\t----\t\t--------------\t\t--------\t-----------
	\tpassword\t%s\t\t\tyes\t\tPassword for connection
	\tPORT\t\t%s\t\t\tyes\t\tPort to bind connection
	\tencoder\t\t%s\t\t\tno\t\tEncoder type		
	\titeration\t%s\t\t\tno\t\tIteration times
	""" %  (choice,argv4,argv3,argv2,argv1)