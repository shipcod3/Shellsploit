#https://en.wikipedia.org/wiki/Shellcode
from color import *


def whatisthis( choice):
	if choice == "Local":
		message = """
Local shellcode is used by an attacker who has limited access to a machine but can exploit a vulnerability,
for example a buffer overflow, in a higher-privileged process on that machine. If successfully executed,
the shellcode will provide the attacker access to the machine with the same higher privileges as the targeted process.
		""" 

	elif choice == "Remote":
		message = """
Remote shellcode is used when an attacker wants to target a vulnerable process running on another machine on a local network or intranet.
If successfully executed, the shellcode can provide the attacker access to the target machine across the network.
		"""

	elif choice == "Download and execute":
		message = """
Download and execute is a type of remote shellcode that downloads and executes some form of malware on the target system. 
This type of shellcode does not spawn a shell, but rather instructs the machine to download a certain executable file off the network, 
save it to disk and execute it. 
		"""

	elif choice == "Egg-hunt":
		message = """
This is another form of staged shellcode, which is used if an attacker can inject a larger shellcode into the process
but cannot determine where in the process it will end up. Small egg-hunt shellcode is injected into the process at a predictable 
location and executed. This code then searches the process's address space for the larger shellcode (the egg) and executes it.
		"""

	print bcolors.RED + bcolors.BOLD + message + bcolors.ENDC