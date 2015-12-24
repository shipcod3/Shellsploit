#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


from core.color import *
from re import findall
from core.Comp import tab


tab.start()
class B3mB4m(object):	
	def __init__(self):
		self.argvlist = ["None", "None", "None", "None"]
		self.disassembly = "None"
		self.mycache = "None"
	def control(self, string):
		bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "ssf" + bcolors.ENDC
		bash += ":"
		bash += bcolors.RED + string+ bcolors.ENDC
		bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
		terminal = raw_input(bash).lower()

		#Injectors
		if string[:9] == "injectors":
			if terminal[:4] == "help":
				from core.help import injectorhelp
				injectorhelp()
				self.control( string)

			elif terminal[:4] == "back":
				pass

			elif terminal[:4] == "exit":
				from sys import exit
				exit()
			
			elif terminal[:4] == "pids":
				from core.commands import pids
				pids( "wholelist")
				self.control( string)

			elif terminal[:6] == "getpid":
				from core.commands import pids
				pids( None, terminal[7:])
				self.control( string)

			elif terminal[:5] == "clear":
				from core.commands import clean
				clean()
				self.control( string)

			#argvlist[0] = PID
			#argvlist[1] = Shellcode
			elif terminal[:3] == "set":
				if terminal[4:7] == "pid":
					self.argvlist[0] = terminal[8:]
				elif terminal[4:13] == "shellcode":
					self.argvlist[1] = terminal[14:]
				
				else:
					if terminal == "":
						self.control( string)
					else:
						print bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC
				self.control( string)


			elif terminal[:12] == "show options":
				#from inject.options import printer		
				if self.argvlist[1] != "None":
					self.mycache = "process"
				if len(self.argvlist[0]) >= len(self.mycache):
					if len(self.argvlist[0]) == 0:
						padd = 8
					elif len(self.argvlist[0]) == 1:
						padd = 8
					elif len(self.argvlist[0]) == 2:
						padd = 8
					else:
						padd = len(self.argvlist[0])+5
				else:
					padd = len(self.mycache)+5

				print """
Module options ({0}):

\tName\t\t{1}\t\tRequired\tDescription
\t----\t\t{2}\t\t--------\t-----------
\tPID\t\t{3}\t\tno\t\tEncoder		
\tShellcode\t{4}\t\tno\t\tEncoder
""".format(string,"Current Setting".ljust(padd),"---------------".ljust(padd),self.argvlist[0].ljust(padd),self.mycache.ljust(padd))
				self.control( string)

			
			#elif terminal[:5] == "disas":
			#	from disassembly.dis import disas
			#	self.disassembly = self.disassembly.replace("\\x", "")

			#	try:
			#		if "64" in string:
			#			print disas( str(bytearray(self.disassembly.decode("hex"))), 64)
			#		elif "86" in string:
			#			print disas( str(bytearray(self.disassembly.decode("hex"))), 32)
			#		else: 
			#			print disas( str(bytearray(self.disassembly.decode("hex"))), 32)
			#	except TypeError:
			#		print "Disassembly failed.Please do not forget report."

			#	self.control( string)
				


			elif terminal[:6] == "inject":
				if string == "injectors/Linux":
					from inject.menager import linux
					#print self.argvlist[1]
					linux( self.argvlist[0], self.argvlist[1].replace('"', "").replace("\\x", ""))
				
				elif string == "injectors/Windows_x86":
					from inject.menager import windows
					windows( self.argvlist[0], self.argvlist[1].replace("\\x", ""))
				self.control( string)

			else:
				if terminal == "":
					self.control( string)
				else:
					print bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC
					self.control( string)


		#Shellcodes
		else:
			
			if terminal[:4] == "help":
				#if terminal[5:11] == "output":
					#from Outputs.exehelp import help
					#print help()
				#else:
					#from core.help import shellcodehelp
					#shellcodehelp()
				from core.help import shellcodehelp
				shellcodehelp()
				self.control( string)
			
			elif terminal[:2] == "os":
				from core.commands import oscommand
				oscommand( terminal[3:])
				self.control( string)

			elif terminal[:4] == "back":
				pass
			
			elif terminal[:4] == "exit":
				from sys import exit
				exit()

			elif terminal[:10] == "whatisthis":
				from core.whatisthis import whatisthis
				if "egg" in string:
					message = "Egg-hunt"
				elif "tcp" in string or "reverse" in string or "netcat" in string:
					message = "Remote"
				elif "download" in string:
					message = "Download and execute"
				else:
					message = "Local"
				#Add special part for particul
				whatisthis( message)
				self.control( string)



				#encoder = argvlist[0]
				#iteration = argvlist[1]
				#file = argvlist[2]
				#That's the rule !
	
			elif terminal[:3] == "set":
				from core.lists import encoders
				#To control whether encoder in list ..


				#files
				list = [
				"freebsd_x86/readfile",
				"linux86/readfile",
				"linux86/chmod",
				"linux86/mkdir",
				"linux86/rmdir",
				"linux64/mkdir",
				"linux64/read",
				"linux_arm/creat",
				"linux_arm/chmod",
				"linux_mips/chmod",
				]

				#Non-params
				list2 = [
				"bsdx64/binsh_spawn",
				"freebsd_x86/killall",
				"linux86/shutdown",
				"linux64/egghunter",
				"linux86/egghunter",
				"linux86/binsh_spawn",
				"linux86/bindash_spawn",
				"linux86/reboot",
				"linux86/killall",
				"linux_arm/killall",
				"linux_arm/binsh_spawn",
				"linux_mips/binsh_spawn",
				"linux_mips/reboot",
				"osx64/binsh_spawn",
				"linux64/binsh_spawn",
				"linux64/shutdown",
				"linux64/reboot",
				"freebsd_x86/binsh_spawn",
				"freebsd_x86/reboot",
				"solarisx86/binsh_spawn",
				"solarisx86/killall",
				"solarisx86/egghunter",
				"solarisx86/bindash_spawn",
				"solarisx86/reboot",
				"solarisx86/shutdown",
				"osx86/binsh_spawn",
				]

				

				if string in list:
					if terminal[4:8] == "file":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						if terminal[12:] not in encoders():
							print "This encoder not in list !"
							self.control( string)
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC

				if string in list2:
					if terminal[4:11] == "encoder":
						if terminal[12:] not in encoders():
							print "This encoder not in list !"
							self.control( string)
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC


				if string == "linux86/netcatbind":
					if terminal[4:8] == "port":
						if not 999 < int(terminal[9:]) <= 9999:
							print "PORT Must be 999-9999 ..."
							self.control( string)
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC	
				
				elif string == "linux86/reverse_telnet":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC

				elif string == "linux86/tcp_bind":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux86/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux86/download&exec":
					if terminal[4:7] == "url":
						self.argvlist[2] = terminal[8:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC									
				


				elif string == "linux64/add_map":
					if terminal[4:6] == "ip":
						self.argvlist[2] = terminal[7:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:7] == "map":
						self.argvlist[3] = terminal[8:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux64/tcp_bind":
					if terminal[4:8].lower() == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux64/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux64/add_user":
					if terminal[4:8] == "user":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "password":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux64/netcatbind":
					if terminal[4:8] == "ip":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "port":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC

				
				elif string == "osx64/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				
				elif string == "osx64/tcp_bind":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC


				elif string == "freebsd_x86/reverse_tcp2":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "freebsd_x86/netcatreverse":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC				
				elif string == "freebsd_x86/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC				
				elif string == "freebsd_x86/add_user":
					if terminal[4:8] == "user":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:12] == "password":
						self.argvlist[3] = terminal[13:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				
				elif string == "freebsd_x86/exec":
					if terminal[4:8] == "command":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC



				elif string == "freebsd_x64/tcp_bind":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:12] == "password":
						self.argvlist[3] = terminal[13:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
			

				elif string == "linux_mips/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux_mips/tcp_bind":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC				
				elif string == "linux_mips/add_user":
					if terminal[4:8] == "user":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "password":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC

				elif string == "linux_arm/add_user":
					if terminal[4:8] == "user":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:12] == "password":
						self.argvlist[3] = terminal[13:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "linux_arm/reverse_tcp":
					if terminal[4:8] == "port":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					elif terminal[4:8] == "host":
						self.argvlist[3] = terminal[9:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC


				elif string == "windows/add_user":
					if terminal[4:8] == "user":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "windows/download&execute":
					if terminal[4:8] == "link":
						self.argvlist[2] = terminal[9:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				elif string == "windows/messagebox":
					if terminal[4:7] == "message":
						self.argvlist[2] = terminal[8:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC
				
				elif string == "windows/exec":
					if terminal[4:11] == "command":
						self.argvlist[2] = terminal[12:]
					elif terminal[4:11] == "encoder":
						self.argvlist[0] = terminal[12:]
					elif terminal[4:13] == "iteration":
						self.argvlist[1] = terminal[14:]
					else:
						print bcolors.RED + bcolors.BOLD + "This option is not available." + bcolors.ENDC

				self.control( string)	

			elif terminal[:12] == "show options":
				from core.SHELLoptions import controlset
				if string[:7] == "linux86":
					if string == "linux86/readfile":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/chmod":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/netcatbind":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/mkdir":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/rmdir":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/tcp_bind":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/reverse_tcp":
						controlset( string, self.argvlist[3], self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/reverse_telnet":
						controlset( string, self.argvlist[3], self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux86/download&exec":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)


				#x86 Solaris will be wait ..
				elif string[:10] == "solarisx86":
					if string == "solarisx86/read":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)
				#solarisx86/bindash_spawn
				#solarisx86/binsh_spawn
				#solarisx86/read
				#solarisx86/reboot
				#solarisx86/shutdown
				#solarisx86/killall


				elif string[:7] == "linux64":
					if string == "linux64/read":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux64/add_map":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[1], self.argvlist[0])
					elif string == "linux64/add_user":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1], self.argvlist[3])						
					elif string == "linux64/mkdir":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux64/tcp_bind":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux64/netcatbind":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])					
					elif string == "linux64/reverse_tcp":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[1], self.argvlist[0])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)
				
				elif string[:5] == "osx86":
					if string == "osx86/tcp_bind":
						#Argvlist[3] == password
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])

					self.control( string)
				

				elif string[:5] == "osx64":
					if string == "osx64/tcp_bind":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "osx64/reverse_tcp":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[0], self.argvlist[1])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					
					self.control( string)

				elif string[:11] == "freebsd_x86":
					if string == "freebsd_x86/reverse_tcp2":
						controlset( string, self.argvlist[3], self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "freebsd_x86/reverse_tcp":
						controlset( string, self.argvlist[3], self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "freebsd_x86/netcatreverse":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[0], self.argvlist[1])						
					elif string == "freebsd_x86/readfile":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "freebsd_x86/exec":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])					
					elif string == "freebsd_x86/add_user":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[0], self.argvlist[1])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)

				elif string[:11] == "freebsd_x64":
					if string == "freebsd_x64/tcp_bind":
						#require password, thats why we need 4 params .. 
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)

				elif string[:9] == "linux_arm":
					if string == "linux_arm/creat":
						controlset( string, self.argvlist[2], self.argvlist[0], self.argvlist[1])
					elif string == "linux_arm/chmod":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2])
					elif string == "linux_arm/add_user":
						controlset( string, self.argvlist[2], self.argvlist[3], self.argvlist[0], self.argvlist[1])
		
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)

				elif string[:10] == "linux_mips":
					if string == "linux_mips/chmod":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2])
					elif string == "linux_mips/reverse_tcp":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					elif string == "linux_mips/add_user":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					elif string == "linux_mips/tcp_bind":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2])
					else:
						controlset( string, self.argvlist[0], self.argvlist[1])
					self.control( string)

				elif string[:7] == "windows":
					if string == "windows/add_user":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					elif string == "windows/messagebox":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2])
					elif string == "windows/exec":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2])
					elif string == "windows/download&execute":
						controlset( string, self.argvlist[0], self.argvlist[1], self.argvlist[2], self.argvlist[3])
					self.control( string)

			elif terminal[:8] == "generate":
				from database.generator import generator
				if string[:7] == "linux86":
					if string == "linux86/killall":
						self.disassembly = generator( "linux_x86", "killall")
					elif string == "linux86/exit":
						self.disassembly = generator( "linux_x86", "exit")
					elif string == "linux86/egghunter":
						self.disassembly = generator( "linux_x86", "egghunter")
					elif string == "linux86/binsh_spawn":
						self.disassembly = generator( "linux_x86", "bin_sh")
					elif string	== "linux86/bindash_spawn":
						self.disassembly = generator( "linux_x86", "bin_dash")
					elif string == "linux86/reboot":
						self.disassembly = generator( "linux_x86", "reboot")
					elif string == "linux86/shutdown":
						self.disassembly = generator( "linux_x86", "shutdown")
					elif string == "linux86/DeleteMBR":
						self.disassembly = generator( "linux_x86", "DeleteMBR")	
					elif string == "linux86/ipv4forward":
						self.disassembly = generator( "linux_x86", "ipv4forward")	
					



					elif string == "linux86/add_user":
						if self.argvlist[2] == "None":
							#Default user name
							self.argvlist[2] == "r00t"
						self.disassembly = generator( "linux_x86", "add_user", self.argvlist[2])
					elif string == "linux86/readfile":
						if self.argvlist[2] == "None":
							print "\nFile name must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "readfile", self.argvlist[2])
					elif string  == "linux86/download&exec":
						if self.argvlist[2] == "None":
							print "\nLink must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "download&exec", self.argvlist[2])


					elif string == "linux86/chmod":
						if self.argvlist[2] == "None":
							print "\nFile name must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "chmod", self.argvlist[2])
					elif string == "linux86/netcatbind":
						if self.argvlist[2] == "None":
							print "\nPORT must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "netcatbind", self.argvlist[2])
					elif string == "linux86/mkdir":
						if self.argvlist[2] == "None":
							print "\nFile name must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "mkdir",  self.argvlist[2])
					elif string == "linux86/rmdir":
						if self.argvlist[2] == "None":
							print "\nFile name must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "rmdir",  self.argvlist[2])
					
					elif string == "linux86/tcp_bind":
						if self.argvlist[2] == "None":
							print "\nPORT must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "tcp_bind", self.argvlist[2])
					elif string == "linux86/reverse_tcp":	
						if self.argvlist[2] == "None" or self.argvlist[3] == "None": 
							print "\nHost&Port must be declared.\n"
							self.control( string)
						self.disassembly = generator( "linux_x86", "reverse_tcp", self.argvlist[3], self.argvlist[2])
					elif string == "linux86/reverse_telnet":
						if self.argvlist[2] == "None" or self.argvlist[3] == "None": 
							print "\nHost&Port must be declared.\n"
							self.control( string)	
						self.disassembly = generator( "linux_x86", "reverse_tcp", self.argvlist[3], self.argvlist[2])

				elif string[:7] == "linux64":
					if string == "linux64/binsh_spawn":
						self.disassembly = generator( "linux_x64", "bin_sh")
					elif string == "linux64/shutdown":
						self.disassembly = generator( "linux_x64", "shutdown")
					elif string == "linux64/reboot":
						self.disassembly = generator( "linux_x64", "reboot")
					elif string == "linux64/mkdir":
						self.disassembly = generator( "linux_x64", "mkdir", self.argvlist[2])
					elif string == "linux64/tcp_bind":
						self.disassembly = generator( "linux_x64", "tcp_bind", self.argvlist[2])
					elif string == "linux64/reverse_tcp":
						self.disassembly = generator( "linux_x64", "reverse_tcp", self.argvlist[2], self.argvlist[3])
					elif string == "linux64/egghunter":
						self.disassembly = generator( "linux_x64", "egghunter")			 
					elif string == "linux64/add_map":
						self.disassembly = generator( "linux_x64", "add_map", self.argvlist[2], self.argvlist[3])	
					elif string == "linux64/add_user":
						self.disassembly = generator( "linux_x64", "add_user")	
					elif string == "linux64/read":
						self.disassembly = generator( "linux_x64", "readfile", self.argvlist[2])	
					elif string == "linux64/netcatbind":
						self.disassembly = generator( "linux_x64", "netcatbind")													


				elif string[:5] == "osx86":
					if string == "osx86/tcp_bind":
						self.disassembly = generator( "osx86", "tcp_bind")
					elif string == "osx86/binsh_spawn":
						self.disassembly = generator( "osx86", "bin_sh")

				elif string[:5] == "osx64":
					if string == "osx64/binsh_spawn":
						self.disassembly = generator( "osx64", "bin_sh")
					elif string == "osx64/tcp_bind":
						self.disassembly = generator( "osx64", "tcp_bind", self.argvlist[2])
					elif string == "osx64/reverse_tcp":
						self.disassembly = generator( "osx64", "reverse_tcp", self.argvlist[3], self.argvlist[2])
				

				elif string[:11] == "freebsd_x86":
					if string == "freebsd_x86/binsh_spawn":
						self.disassembly = generator( "freebsd_x86", "bin_sh")
					elif string == "freebsd_x86/reboot":
						self.disassembly = generator( "freebsd_x86", "reboot")
					elif string == "freebsd_x86/killall":
						self.disassembly = generator( "freebsd_x86", "killall")
					elif string == "freebsd_x86/add_user":
						self.disassembly = generator( "freebsd_x86", "add_user", self.argvlist[2], self.argvlist[3])
					elif string == "freebsd_x86/read":
						self.disassembly = generator( "freebsd_x86", "read", self.argvlist[2])
					elif string == "freebsd_x86/netcatreverse":
						self.disassembly = generator( "freebsd_x86", "netcatreverse", self.argvlist[3], self.argvlist[2])
					elif string == "freebsd_x86/reverse_tcp":
						self.disassembly = generator( "freebsd_x86", "reverse_tcp")
					elif string == "freebsd_x86/reverse_tcp2":
						self.disassembly = generator( "freebsd_x86", "reverse_tcp2")
					elif string == "freebsd_x86/exec":
						self.disassembly = generator( "freebsd_x86", "exec")

				elif string[:11] == "freebsd_x64":
					if string == "freebsd_x64/binsh_spawn":
						self.disassembly = generator( "freebsd_x64", "bin_sh")
					elif string == "freebsd_x64/tcp_bind":
						self.disassembly = generator( "freebsd_x64", "tcp_bind", self.argvlist[2], self.argvlist[3])

				elif string[:9] == "linux_arm":
					if string == "linux_arm/chmod":
						self.disassembly = generator( "linux_arm", "chmod", self.argvlist[2])
					elif string == "linux_arm/binsh_spawn":
						self.disassembly = generator( "linux_arm", "bin_sh")
					elif string == "linux_arm/killall":
						self.disassembly = generator( "linux_arm", "killall")
					elif string == "linux_arm/creat":
						self.disassembly = generator( "linux_arm", "creat", self.argvlist[2])
					elif string == "linux_arm/add_user":
						self.disassembly = generator( "linux_arm", "add_user", self.argvlist[3], self.argvlist[2])
					elif string == "linux_arm/reverse_tcp":
						self.disassembly = generator( "linux_arm", "reverse_tcp")

				elif string[:10] == "linux_mips":
					if string == "linux_mips/reverse_tcp":
						self.disassembly = generator( "linux_mips", "reverse_tcp")
					elif string == "linux_mips/binsh_spawn":
						self.disassembly = generator( "linux_mips", "bin_sh")
					elif string == "linux_mips/reboot":
						self.disassembly = generator( "linux_mips", "reboot")
					elif string == "linux_mips/chmod":
						self.disassembly = generator( "linux_mips", "chmod")
					elif string == "linux_mips/add_user":
						self.disassembly = generator( "linux_mips", "add_user")
					elif string == "linux_mips/tcp_bind":
						self.disassembly = generator( "linux_mips", "tcp_bind")


				elif string[:7] == "windows":
					if string == "windows/add_user":
						self.disassembly = generator( "windows", "reverse_tcp")
					elif string == "windows/messagebox":
						self.disassembly = generator( "windows", "messagebox")
					elif string == "windows/download&execute":
						self.disassembly = generator( "windows", "downloandandexecute")
					elif string == "windows/exec":
						self.disassembly = generator( "windows", "exec", self.argvlist[2])
			
				#Solaris will be sleep little bit ..
				elif string[:10] == "solarisx86":
					from disassembly.Syscalls import linux_32
					from disassembly.Syscalls import solaris_32
					
					if string == "solarisx86/binsh_spawn":
						self.disassembly = generator( "linux_x86", "bin_sh")
					elif string == "solarisx86/killall":
						self.disassembly = generator( "linux_x86", "killall")
					elif string == "solarisx86/egghunter":
						self.disassembly = generator( "linux_x86", "egghunter")
					elif string	== "solarisx86/bindash_spawn":
						self.disassembly = generator( "linux_x86", "bin_dash")
					elif string == "solarisx86/reboot":
						self.disassembly = generator( "linux_x86", "reboot")
					elif string == "solarisx86/shutdown":
						self.disassembly = generator( "linux_x86", "shutdown")

					self.disassembly = self.disassembly.replace("\\x", "")
					self.disassembly = self.disassembly.replace("b00b", "b0"+solaris_32.SolarisSystemcall( linux_32.i386Systemcall( str(int("b",16))), True))
					self.disassembly = self.disassembly.replace("cd80", "cd"+solaris_32.SolarisInterrupted())
					qe = findall("..?", self.disassembly)
					self.disassembly = "\\x"+"\\x".join(qe).lower()

					if string == "solarisx86/read":
						if self.argvlist[2] == "None":
							print "\nFile name must be declared.\n"
							self.control( string)
						self.disassembly = generator( "solarisx86", "readfile", self.argvlist[2])



				if self.argvlist[0] == "x86/xor_b3m":
					from encoders.xor_b3m import prestart
					if self.argvlist[1] == "None":
						self.argvlist[1] = 1
					elif self.argvlist[1] == 0:
						self.argvlist[1] = 1
					self.disassembly = prestart( self.disassembly.replace("\\x", ""), int(self.argvlist[1]))

				elif self.argvlist[0] == "x86/xor":
					from encoders.xor import prestart
					if self.argvlist[1] == "None":
						self.argvlist[1] = 1
					elif self.argvlist[1] == 0:
						self.argvlist[1] = 1
					self.disassembly = prestart( self.disassembly.replace("\\x", ""), int(self.argvlist[1]))

				else:
					self.disassembly = self.disassembly	

				#Error on too big iterations
				#print "\n"+"Shellcode Lenght : %d" % len(str(bytearray(self.disassembly.replace("\\x", "").decode("hex"))))
				print "\n"+self.disassembly+"\n"
				self.control( string)


			elif terminal[:6] == "output":
				if self.disassembly == "None":
					print "Please generate shellcode before save it."
					self.control( string)	

				#I'm not sure about this option, should I get this option with params 
				#Or directly inputs ? ..
				if terminal[7:10].lower() == "exe":
					#Will be add missing parts ..
					if "linux86" in terminal.lower():
						OS = "linux86"
					elif "linux64" in terminal.lower():
						OS= "linux64"
					elif "windows" in terminal.lower():
						OS = "windows"
					elif "freebsdx86" in terminal.lower():
						OS = "freebsdx86"
					elif "freebsdx64" in terminal.lower():
						OS = "freebsdx64"
					elif "openbsdx86" in terminal.lower():
						OS = "openbsdx86"
					elif "solarisx86" in terminal.lower():
						OS = "solarisx86"
					elif "linuxpowerpc" in terminal.lower():
						OS = "linuxpowerpc"
					elif "openbsdpowerpc" in terminal.lower():
						OS = "openbsdpowerpc"			
					elif "linuxsparc" in terminal.lower():
						OS = "linuxsparc"
					elif "freebsdsparc" in terminal.lower():
						OS = "freebsdsparc"
					elif "openbsdsparc" in terminal.lower():
						OS = "openbsdsparc"
					elif "solarissparc" in terminal.lower():
						OS = "solarissparc"
					elif "linuxarm" in terminal.lower():
						OS = "linuxarm"
					elif "freebsdarm" in terminal.lower():
						OS = "freebsdarm"
					elif "openbsdarm" in terminal.lower():
						OS = "openbsdarm"
					else:
						OS = None
					
			
					from Outputs.exe import ExeFile
					ExeFile( self.disassembly, OS)
					self.control( string)


				elif terminal[7:10].lower() == "c++" or terminal[7:10].lower() == "cpp":
					from Outputs.Cplusplus import CplusplusFile
					if "windows" in string:
						CplusplusFile( self.disassembly, True)
					else:
						CplusplusFile( self.disassembly)
				
				elif terminal[7:8].lower() == "c":
					if "windows" in string:
						from Outputs.Cplusplus import CplusplusFile
						CplusplusFile( self.disassembly, True)
					else:
						from Outputs.C import CFile
						CFile( self.disassembly)				

				elif terminal[7:9].lower() == "py" or terminal[7:13].lower() == "python": 
					from Outputs.python import PyFile
					PyFile( self.disassembly)
				
				elif terminal[7:10].lower() == "txt":
					from Outputs.txt import TxtFile
					TxtFile( self.disassembly)	


				else:
					print bcolors.RED + bcolors.BOLD + "[-] Unknown output type: %s" % terminal + bcolors.ENDC
				self.control( string)					

			elif terminal[:5] == "clear":
				from core.commands import clean
				clean()
				self.control( string)

			elif terminal[:2].lower() == "ip":
				from core.commands import IP 
				IP()
				self.control( string)

			elif terminal[:13] == "show encoders":
				from core.lists import encoderlist
				encoderlist()
				self.control( string)

			elif terminal[:5] == "disas":
				if self.disassembly == "None":
					print "Shellcode must be generate before disassembly !"

				else:
					from disassembly.dis import disas
					self.disassembly = self.disassembly.replace("\\x", "")
					if "linux_mips" not in string or "linux_mips" not in string:
						try:
							if "64" in string:
								#The goal of diStorm3 is to decode x86/AMD64 binary streams and return a structure that describes each instruction.
								print disas( str(bytearray(self.disassembly.decode("hex"))), 64)
							elif "86" in string:
								print disas( str(bytearray(self.disassembly.decode("hex"))), 32)
							else: #Just for a while
								print disas( str(bytearray(self.disassembly.decode("hex"))), 32)
						except TypeError:
							print "Disassembly failed.Please do not forget report."
					else:
						print "Not support this disassembly type !"
				self.control( string)

			else:
				if terminal == "":
					self.control( string)
				else:
					print bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC
					self.control( string)
