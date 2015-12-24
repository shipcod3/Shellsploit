def exit():
	return "\\x31\\xc0\\x40\\xcd\\x80"


"""
Linux x86 - 5 bytes

08048060 <.text>:
 8048060:	31 c0                	xor    %eax,%eax
 8048062:	40                   	inc    %eax
 8048063:	cd 80                	int    $0x80
"""

