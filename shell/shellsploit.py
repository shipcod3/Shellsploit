#!/usr/bin/env python

#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import os

name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)



from control import *
from core.logo.logo import banner
from core.logo.counter import *
#import signal
from core.Comp import tab


tab.start(1)
db = B3mB4mLogo().start()
def start():
	#Dynamic counter for shellcodes,injectors etc..
	print (banner( db[0], db[1], db[2], db[3]))
	shellsploit()

def shellsploit():
	try:
		bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "ssf" + bcolors.ENDC
		bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
		#terminal = raw_input(bash).lower()
		try:
			terminal = raw_input(bash)
		except NameError:
			terminal = input(bash)

		if terminal[:4] == "help":
			from core.help import mainhelp
			mainhelp()
			shellsploit()

		elif terminal[:14] == "show backdoors":
			from core.help import mainhelp

		elif terminal[:2] == "os":
			from core.commands import oscommand
			oscommand( terminal[3:])
			shellsploit()


		elif terminal[:6] == "banner":
			print (banner( db[0], db[1], db[2], db[3]))
			shellsploit()

		elif terminal[:3] == "use":
			if terminal[4:len("linux86/binsh_spawn")+4] == "linux86/binsh_spawn":
				B3mB4m().control( "linux86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux86/read")+4] == "linux86/read":
				B3mB4m().control( "linux86/read")
				shellsploit()
			elif terminal[4:len("linux86/chmod")+4] == "linux86/chmod":
				B3mB4m().control( "linux86/chmod")
				shellsploit()
			elif terminal[4:len("linux86/tcp_bind")+4] == "linux86/tcp_bind":
				B3mB4m().control( "linux86/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux86/reverse_tcp")+4] == "linux86/reverse_tcp":
				B3mB4m().control( "linux86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux86/exec")+4] == "linux86/exec":
				B3mB4m().control( "linux86/exec")
				shellsploit()
			#elif terminal[4:len("linux86/download&exec")+4] == "linux86/download&exec":
				#B3mB4m().control( "linux86/download&exec")
				#shellsploit()


			elif terminal[4:len("linux64/read")+4] == "linux64/read":
				B3mB4m().control( "linux64/read")
				shellsploit()
			elif terminal[4:len("linux64/binsh_spawn")+4] == "linux64/binsh_spawn":
				B3mB4m().control( "linux64/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux64/tcp_bind")+4] == "linux64/tcp_bind":
				B3mB4m().control( "linux64/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux64/reverse_tcp")+4] == "linux64/reverse_tcp":
				B3mB4m().control( "linux64/reverse_tcp")
				shellsploit()

			elif terminal[4:len("linux/binsh_spawn")+4] == "linux/binsh_spawn":	
				B3mB4m().control( "linux/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux/tcp_bind")+4] == "linux/tcp_bind":	
				B3mB4m().control( "linux/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux/reverse_tcp")+4] == "linux/reverse_tcp":	
				B3mB4m().control( "linux/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux/read")+4] == "linux/read":	
				B3mB4m().control( "linux/read")
				shellsploit()

				

			elif terminal[4:len("osx86/tcp_bind")+4] == "osx86/tcp_bind":
				B3mB4m().control( "osx86/tcp_bind")
				shellsploit()
			elif terminal[4:len("osx86/binsh_spawn")+4] == "osx86/binsh_spawn":
				B3mB4m().control( "osx86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("osx86/reverse_tcp")+4] == "osx86/reverse_tcp":
				B3mB4m().control( "osx86/reverse_tcp")
				shellsploit()


			elif terminal[4:len("osx64/reverse_tcp")+4] == "osx64/reverse_tcp":
				B3mB4m().control( "osx64/reverse_tcp")
				shellsploit()
			elif terminal[4:len("osx64/tcp_bind")+4] == "osx64/tcp_bind":
				B3mB4m().control( "osx64/tcp_bind")
				shellsploit()
			elif terminal[4:len("osx64/binsh_spawn")+4] == "osx64/binsh_spawn":
				B3mB4m().control( "osx64/binsh_spawn")
				shellsploit()



			elif terminal[4:len("FreeBSDx86/binsh_spawn")+4] == "FreeBSDx86/binsh_spawn":
				B3mB4m().control( "freebsd_x86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/reverse_tcp2")+4] == "FreeBSDx86/reverse_tcp2":
				B3mB4m().control( "freebsd_x86/reverse_tcp2")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/reverse_tcp")+4] == "FreeBSDx86/reverse_tcp":
				B3mB4m().control( "freebsd_x86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/read")+4] == "FreeBSDx86/read":
				B3mB4m().control( "freebsd_x86/read")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/exec")+4] == "FreeBSDx86/exec":
				B3mB4m().control( "freebsd_x86/exec")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/tcp_bind")+4] == "FreeBSDx86/tcp_bind":
				B3mB4m().control( "freebsd_x86/tcp_bind")
				shellsploit()


			elif terminal[4:len("FreeBSDx64/binsh_spawn")+4] == "FreeBSDx64/binsh_spawn":
				B3mB4m().control( "freebsd_x64/binsh_spawn")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/tcp_bind")+4] == "FreeBSDx64/tcp_bind":
				B3mB4m().control( "freebsd_x64/tcp_bind")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/reverse_tcp")+4] == "FreeBSDx64/reverse_tcp":
				B3mB4m().control( "freebsd_x64/reverse_tcp")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/exec")+4] == "FreeBSDx64/exec":
				B3mB4m().control( "freebsd_x64/exec")
				shellsploit()
  

			elif terminal[4:len("linux_arm/binsh_spawn")+4] == "linux_arm/binsh_spawn":
				B3mB4m().control( "linux_arm/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux_arm/chmod")+4] == "linux_arm/chmod":
				B3mB4m().control( "linux_arm/chmod")
				shellsploit()           
			elif terminal[4:len("linux_arm/reverse_tcp")+4] == "linux_arm/reverse_tcp":
				B3mB4m().control( "linux_arm/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux_arm/exec")+4] == "linux_arm/exec":
				B3mB4m().control( "linux_arm/exec")
				shellsploit()
			
		

			elif terminal[4:len("linux_mips/binsh_spawn")+4] == "linux_mips/binsh_spawn":
				B3mB4m().control( "linux_mips/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux_mips/chmod")+4] == "linux_mips/chmod":
				B3mB4m().control( "linux_mips/chmod")
				shellsploit()
			elif terminal[4:len("linux_mips/reverse_tcp")+4] == "linux_mips/reverse_tcp":
				B3mB4m().control( "linux_mips/reverse_tcp")
				shellsploit() 
			elif terminal[4:len("linux_mips/tcp_bind")+4] == "linux_mips/tcp_bind":
				B3mB4m().control( "linux_mips/tcp_bind")
				shellsploit()

			#elif windows/reverse_tcp
			#elif windows/tcp_bind
			elif terminal[4:len("windows/messagebox")+4] == "windows/messagebox":
				B3mB4m().control( "windows/messagebox")
				shellsploit()
			elif terminal[4:len("windows/download&execute")+4] == "windows/download&execute":
				B3mB4m().control( "windows/download&execute")
				shellsploit()
			elif terminal[4:len("windows/exec")+4] == "windows/exec":
				B3mB4m().control( "windows/exec")
				shellsploit()

			elif terminal[4:len("solarisx86/binsh_spawn")+4] == "solarisx86/binsh_spawn":
				B3mB4m().control( "solarisx86/binsh_spawn")
				shellsploit()                                  
			elif terminal[4:len("solarisx86/read")+4] == "solarisx86/read":
				B3mB4m().control( "solarisx86/read")
				shellsploit()    
			elif terminal[4:len("solarisx86/reverse_tcp")+4] == "solarisx86/reverse_tcp":
				B3mB4m().control( "solarisx86/reverse_tcp")
				shellsploit()    
			elif terminal[4:len("solarisx86/tcp_bind")+4] == "solarisx86/tcp_bind":
				B3mB4m().control( "solarisx86/tcp_bind")
				shellsploit()    
		 

			elif terminal[4:len("injectors/Windows_x86")+4] == "injectors/Windows_x86":
				B3mB4m().control( "injectors/Windows_x86")
				shellsploit()
			elif terminal[4:len("injectors/Linux")+4] == "injectors/Linux":
				B3mB4m().control( "injectors/Linux")
				shellsploit()    


			else:
				print ("\nModule not avaible !\n")
				shellsploit()


		elif terminal[:14] == "show injectors":
			from core.lists import injectorlist
			injectorlist()
			shellsploit()

		elif terminal[:5] == "clear":
			from core.commands import clean
			clean()
			shellsploit()

		elif terminal[:12] == "show modules":
			from core.shellcodes import shellcodelist
			shellcodelist()
			shellsploit()    


		elif terminal[:4] == "exit":
			exit("\nThanks for using shellsploit !\n")    

		else:
			if terminal == "":
				shellsploit()
			else:
				print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC)
				shellsploit()



	except(KeyboardInterrupt):
		print("\n[*] (Ctrl + C ) Detected, Trying To Exit ...")
		from sys import exit
		exit()
	  


def main():
	import optparse 
	parser = optparse.OptionParser()
	parser.add_option('-p', '--payload', action="store")
	parser.add_option('-o', '--output', action="store", default=True)
	parser.add_option('-l','--list', action="store", default=True)
	parser.add_option('-n','--nc', action="store", default=True)
	parser.add_option('--host', action="store")
	parser.add_option('--port', action="store")
	(options, args) = parser.parse_args()
	

	if options.list == "backdoors":
		from core.backdoors import backdoorlist
		backdoorlist( require=False)
		
	elif options.nc == "netcat" or options.nc == "nc":
		from Session.netcat import nc
		if options.port:
			nc( PORT)
		else:
			nc()
	else:
		if options.payload:
			if options.host and options.port:
				from core.backdoors import backdoorlist
				if options.payload in backdoorlist( require=True):
					from Session.generator import process
					if options.output:
						process( options.payload, options.host, options.port, options.output)
					else:
						process( options.payload, options.host, options.port, True)
						#Default, file will be create with random name.
				else:
					print ("\npython shellsploit  -p PAYLOAD --host IP --port P0RT\n")
			else:
				print ("\npython shellsploit  -p PAYLOAD --host IP --port P0RT\n")
		else:
			start()
